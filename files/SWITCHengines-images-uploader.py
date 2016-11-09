#!/usr/bin/env python
#
#  Copyright (c) 2015-2016 SWITCH http://www.switch.ch
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# Author: Valery Tschopp <valery.tschopp@switch.ch>
# Date: 2016-11-09

import argparse
import datetime
import logging
import os
import os.path
import sys

# see https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
import requests
requests.packages.urllib3.disable_warnings()

# OpenStack clients lib
from glanceclient.v2 import client as glance_client
from keystoneauth1.identity import v3 as identity_v3
from keystoneauth1 import session
import keystoneclient
from keystoneclient.v3 import client as keystone_v3

#
# info from distrosInfo.py file
#
from distrosInfo import images_info
from distrosInfo import description_deprecated


def get_environ(key, verbose=False):
    if key not in os.environ:
        print "ERROR:", key, "not define in environment"
        sys.exit(1)
    if verbose:
        if 'password' in key.lower():
            key_value = '*' * len(os.environ[key])
        else:
            key_value = os.environ[key]
        print "{}: {}".format(key, key_value)
    return os.environ[key]


# logger
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(levelname)s: %(message)s')
# disable the other loggers (requests.*, ...)
for handler in logging.root.handlers:
    handler.addFilter(logging.Filter('main'))
logger = logging.getLogger('main')


def main():

    # constants
    DEFAULT_IMAGES_LOCATION = '/usr/share/nginx/html/images'

    # parse args
    parser = argparse.ArgumentParser(description="SWITCHengines Images Uploader")
    parser.add_argument('--os-auth-url', help='OpenStack auth URL')
    parser.add_argument('--os-username', help='OpenStack username')
    parser.add_argument('--os-password', help='OpenStack user password')
    parser.add_argument('--os-tenant-name', help='OpenStack tenant name')
    parser.add_argument('--os-region-name', help='OpenStack region name')

    parser.add_argument('-a', '--all-regions',
                        action='store_true',
                        help='Upload images in all regions. Default only in --os-region-name|OS_REGION_NAME')

    parser.add_argument('--prefix',
                        help='Prefix for the images names (e.g. test_)')

    parser.add_argument('-l', '--images-location',
                        help="Location of the raw images (It could be an URL). Default: {}".format(DEFAULT_IMAGES_LOCATION))

    parser.add_argument('-v','--verbose', help='verbose mode', action='store_true')
    parser.add_argument('-d','--debug', help='debug mode', action='store_true')
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.INFO)
    if args.debug:
        logger.setLevel(logging.DEBUG)

    # validate args
    if not args.images_location and not os.path.exists(DEFAULT_IMAGES_LOCATION):
        logger.error("Location of the raw images not defined (-l|--images-location) and default local directory {} does not exist!".format(DEFAULT_IMAGES_LOCATION))
        sys.exit(1)

    if not args.os_auth_url and not os.environ.get('OS_AUTH_URL'):
        logger.error("Keystone auth URL missing (--os-auth-url param or env OS_AUTH_URL)")
        sys.exit(1)

    if not args.os_username and not os.environ.get('OS_USERNAME'):
        logger.error("ERROR: OpenStack username missing (--os-username param or env OS_USERNAME)")
        sys.exit(1)

    if not args.os_password and not os.environ.get('OS_PASSWORD'):
        logger.error("ERROR: OpenStack user password missing (--os-password param or env OS_PASSWORD)")
        sys.exit(1)

    if not args.os_tenant_name and not os.environ.get('OS_TENANT_NAME'):
        logger.error("ERROR: OpenStack tenant name missing (--os-tenant-name param or env OS_TENANT_NAME)")
        sys.exit(1)

    if not args.os_region_name and not os.environ.get('OS_REGION_NAME'):
        logger.error("ERROR: OpenStack region name missing (--os-region-name param or env OS_REGION_NAME)")
        sys.exit(1)


    #
    # images
    #
    images_location = args.images_location if args.images_location else DEFAULT_IMAGES_LOCATION
    images_name_prefix = args.prefix

    #
    # Openstack credentials
    #
    os_auth_url = args.os_auth_url if args.os_auth_url else get_environ('OS_AUTH_URL')
    os_username = args.os_username if args.os_username else get_environ('OS_USERNAME')
    os_password = args.os_password if args.os_password else get_environ('OS_PASSWORD')
    os_tenant_name = args.os_tenant_name if args.os_tenant_name else get_environ('OS_TENANT_NAME')
    os_region_name = args.os_region_name if args.os_region_name else get_environ('OS_REGION_NAME')

    # keystone client
    if '/v2.0' in os_auth_url:
        os_auth_url_v3 = os_auth_url.replace('/v2.0', '/v3')
    else:
        os_auth_url_v3 = os_auth_url

    auth = identity_v3.Password(auth_url=os_auth_url_v3,
                                username=os_username,
                                password=os_password,
                                project_name=os_tenant_name,
                                user_domain_name='default',
                                project_domain_name='default')
    auth_session = session.Session(auth=auth)
    keystone = keystone_v3.Client(session=auth_session)

    # get tenant id
    try:
        tenant = keystone.projects.find(name=os_tenant_name)
    except keystoneclient.exceptions.NotFound as e:
        logger.error("Looking up tenant id for '{}' failed".format(os_tenant_name))
        sys.exit(1)
    os_tenant_id = tenant.id

    # which regions to use, see -a|--all-regions option
    regions = [os_region_name]
    if args.all_regions:
        # get all regions
        all_region_names = []
        for region in keystone.regions.list():
            all_region_names.append(region.id)
        if os_region_name in all_region_names:
            regions = all_region_names

    logger.debug("regions: {}".format(regions))

    #
    # for each region do
    #
    return_code = 0
    for region in regions:
        logger.info("Uploading images to region: {}".format(region))

        # glance client for region
        glance = glance_client.Client(session=auth_session, region_name=region)

        # create all the distro (images_info)
        for distro_name in images_info:

            image_info = images_info[distro_name]
            image_name = image_info['image_name']

            logger.info("Processing {}@{}...".format(distro_name,region))
            logger.debug("image_info: {}".format(image_info))

            # existing image(s) to replace
            existing_owned_public_images = glance_list_owned_public_images(glance, os_tenant_id, image_info)
            for eop_image in existing_owned_public_images:
                logger.debug("existing public image: '{}' [{}]".format(eop_image.name,
                                                                       eop_image.id,
                                                                       eop_image.visibility))

            # create/upload the new image
            logger.info("Creating and uploading new image '{}'".format(image_name))
            rc = glance_create_new_image(glance, images_location, image_info, images_name_prefix)
            if rc != 0:
                return_code += 1
                logger.error("{}@{}: New image '{}' -> '{}' not created!".format(distro_name,
                                                                                 region,
                                                                                 image_info['image_raw_source'],
                                                                                 image_name))
            else:
                for eop_image in existing_owned_public_images:

                    now_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    new_name = "{}-{}".format(eop_image.name, now_datetime)

                    logger.info("Set existing image '{}' to private '{}'".format(eop_image.name, new_name))

                    rc = glance_image_set_private(glance, eop_image, new_name, description_deprecated)
                    if rc != 0:
                        return_code += 1
                        logger.error("{}@{}: Updating image '{} [{}]' to private '{}' failed!".format(distro_name,
                                                                                                      region,
                                                                                                      new_name,
                                                                                                      eop_image.name,
                                                                                                      eop_image.id))


    return return_code

def glance_list_owned_public_images(glance, owner_id, image_info):
    """
    Get a list of owned public images with the "same" name
    The name is a 'in' match function. e.i. 'TOTO' matches 'test_TOTO' or 'TOTO - 2016-10-03'
    :param glance: glance client
    :param owner_id: owner id
    :param image_info: image_info dictionary
    :return: list of public images, owned by owner_id, with the same name
    """

    images = []
    list_kwargs = {'filters': {'visibility': 'public', 'owner': owner_id}}
    public_owned_images = glance.images.list(**list_kwargs)
    for image in public_owned_images:
        # only images with the "same" name ('TOTO' matches 'test_TOTO' or 'TOTO - 2016-10-03')
        if image_info['image_name'] in image.name:
            images.append(image)
    return images


def glance_create_new_image(glance, images_location, image_info, image_name_prefix=None):
    """
    Creates a new Glance public image
    :param glance: glance client
    :param images_location: location of the raw image source
    :param image_info: image_info dictionary
    :param image_name_prefix: image name prefix to add
    :return: 0 on success, >0 on error
    """
    # image raw file path
    image_raw_source = image_info['image_raw_source']
    image_file = os.path.join(images_location, image_raw_source)

    if not os.path.isfile(image_file):
        logger.warning("image raw file:'{}' not found!".format(image_file))
        return 1

    fimg = None
    try:
        fimg = open(image_file, 'rb')
    except Exception as e:
        logger.error("Opening raw image file:'{}' failed".format(image_file))
        return 1

    try:
        # image name
        image_name = image_info['image_name']
        if image_name_prefix:
            image_name = "{}{}".format(image_name_prefix,image_name)
        logger.debug("image_name: {}".format(image_name))

        # image min_disk
        if image_info['image_min_disk'] == 'auto':
            # compute the size of the file -> min disk size in GB
            imagesize = os.fstat(fimg.fileno()).st_size
            image_min_disk = (imagesize/1024/1024/1024)+1
        else:
            image_min_disk = image_info['image_min_disk']
        logger.debug("image_min_disk: {}".format(image_min_disk))

        # image min_ram
        image_min_ram = image_info['image_min_ram']
        logger.debug("image_min_ram: {}".format(image_min_ram))

        # image properties (dictionary)
        image_properties = image_info['image_properties']
        logger.debug("image_properies: {}".format(image_properties))

        logger.debug("glance image create (private): '{}'".format(image_name))
        image = glance.images.create(name=image_name,
                                     visibility='private',
                                     disk_format='raw',
                                     container_format='bare',
                                     min_disk=int(image_min_disk),
                                     min_ram=int(image_min_ram))
        logger.debug("glance image upload: '{}' -> '{}'".format(fimg.name, image_name))
        glance.images.upload(image.id, fimg)
        logger.debug("glance image update: visibility=public, properties={}".format(image_properties))
        image_properties.update(visibility='public')
        glance.images.update(image.id, **image_properties)

    except Exception as e:
        logger.exception("Creating new Glance image '{}' failed".format(image_name))
        return 1

    return 0


def glance_image_set_private(glance, image, new_name, new_description):
    """
    Set the image to private, with a new name and new description
    :param glance: glance client
    :param image: image
    :param new_name: new name for image
    :param new_description: new description for image
    :return: 0 on success, >0 on error
    """
    try:
        glance.images.update(image_id=image.id,
                             visibility='private',
                             name=new_name,
                             description=new_description)
    except Exception as e:
        logger.exception("Updating Glance image '{}' [{}] -> '{}' failed: {}".format(image.name, image.id,
                                                                                     new_name))
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
