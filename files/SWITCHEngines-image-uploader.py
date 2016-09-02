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
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


from multiprocessing import Process
from subprocess import Popen
import threading
import thread
import argparse
import os
import subprocess
import sys

GLANCE_COMMAND='/usr/bin/glance'

def main():


    # parse args
    parser = argparse.ArgumentParser(description="glanceCron managament tool")
    parser.add_argument('-A','--user', help='User name')
    parser.add_argument('-V','--version', help='show version and exit', action='store_true')
    parser.add_argument('-P','--password', help='User password')
    parser.add_argument('-K','--keystone', help='Keystone contact point url')
    parser.add_argument('-T','--tenant', help='User tenant')
    parser.add_argument('-TID','--tenantId', help='User tenant id')
    parser.add_argument('-R','--regions', help='Regions names')
    parser.add_argument('-C','--singleDistros',
                        help='DISTROS info file (optional). If not specified, the default /home/ubuntu/distrosInfo is used instead')
    parser.add_argument('-D','--distros',
                        help=' DISTROS (optional) specified within quotes (e.g. \"ubuntu debian\"). If not specified, the distros defined in the DISTROS info file are used')
    parser.add_argument('-Text','--text',
                        help='Text to add as a prefix to the images names (e.g. test)')
    parser.add_argument('-U','--url',
                        help='Url of the location where the raw images are to be found. Default is local directory `/usr/share/nginx/html/SWITCHengines/`')
    args = parser.parse_args()


    # validate args
    global url
    if not args.url and not os.path.exists('/usr/share/nginx/html/images/'):
        print("ERROR: Url location of the raw images not defined, and default local directory `/usr/share/nginx/html/images/` does not exist!")
        sys.exit(1)
    else:
        url = args.url if args.url else '/usr/share/nginx/html/images/'

    if not args.user and not os.environ['OS_USERNAME']:
        print("ERROR: User name missing")
        sys.exit(1)

    if not args.password and not os.environ['OS_PASSWORD']:
        print("ERROR: User password missing")
        sys.exit(1)

    if not args.keystone and not os.environ['OS_AUTH_URL']:
        print("ERROR: Keystone contact point url missing")
        sys.exit(1)

    if not args.regions and not os.environ['OS_REGION_NAME']:
        print("ERROR: Regions missing")
        sys.exit(1)

    if not args.tenant and not os.environ['OS_TENANT_NAME']:
        print("ERROR: Tenant name missing")
        sys.exit(1)

    if not args.text:
        text=""
    else:
        text=args.text

    # IMPORTANT: distrosInfo provides ALL the maps that are used. This
    # is also why it is sourced by default!

    import distrosInfo

    global description_old

    distros=[]
    descriptionsMap={}
    descriptionsMapLong={}
    description_old = distrosInfo.description_old
    for k in distrosInfo.distrosMap:
        distros.append(k)
        descriptionsMap[k]=distrosInfo.distrosMap[k][1]
        descriptionsMapLong[k]=distrosInfo.distrosMap[k][5]

    if  args.distros:
        distros=[args.distros]

    engines_names = {}
    for i in distros:
        engines_names[i]=text + descriptionsMap[i]

    import datetime
    from datetime import timedelta

    global today
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    get_keystone_creds()
    for region in [args.regions] if args.regions else [os.environ["OS_REGION_NAME"]]:
        os.environ["OS_REGION_NAME"]=region
        Exec(region,distros,descriptionsMapLong,engines_names)

def get_keystone_creds():
    global keystone_authtoken_user
    global keystone_authtoken_auth_url
    global keystone_authtoken_user_password
    global os_region_name
    global keystone_authtoken_user_tenant_name
    keystone_authtoken_user=os.environ['OS_USERNAME']
    keystone_authtoken_auth_url=os.environ['OS_AUTH_URL']
    keystone_authtoken_user_password=os.environ['OS_PASSWORD']
    os_region_name=os.environ['OS_REGION_NAME']
    keystone_authtoken_user_tenant_name = os.environ['OS_TENANT_NAME']
    #d = {}
    #d['username'] = os.environ['OS_USERNAME']
    #d['password'] = os.environ['OS_PASSWORD']
    #d['auth_url'] = os.environ['OS_AUTH_URL']
    #d['tenant_name'] = os.environ['OS_TENANT_NAME']

def glanceImagesIds(name):

    from glanceclient.v2 import client as glclient
    from keystoneclient import session
    from keystoneclient.v2_0 import client as keystone_client
    import re
    import pprint

    keystone = keystone_client.Client(auth_url=keystone_authtoken_auth_url,
                       username=keystone_authtoken_user,
                       password=keystone_authtoken_user_password,
                       tenant_name=keystone_authtoken_user_tenant_name)

    # get tenant id from keystone
    global os_tenant_id
    tenant = keystone.tenants.find(name=keystone_authtoken_user_tenant_name)
    os_tenant_id = tenant.id

    glance_endpoint = keystone.service_catalog.url_for(service_type='image',
                                                       endpoint_type='publicURL',region_name=os_region_name)
    glance = glclient.Client(endpoint=glance_endpoint,token=keystone.auth_token)
    try:
        glance_output=glance.images.list()
    except Exception as e:
        print("Error in image list %s" % e.message)
        #os._exit(1)

    existingImages = {}
    #existingImagesID = []
    #existingImagesOwner = []
    #existingImagesVisibilityFlag = []
    #existingImagesProtectionFlag = []
    for line in glance_output:
        if name in line.name.encode('UTF8') :
            existingImages[line.id] = { 'name':line.name , 'owner':line.owner,'visibility':line.visibility,'protected':line.protected }
    return existingImages

#def glanceImageShow(id):
#    from glanceclient.v2 import client as glclient
#    from keystoneclient import session
#    from keystoneclient.v2_0 import client as keystone_client
#    import re
#    import pprint
#
#    keystone = keystone_client.Client(auth_url=keystone_authtoken_auth_url,
#                       username=keystone_authtoken_user,
#                       password=keystone_authtoken_user_password,
#                       tenant_name=keystone_authtoken_user_tenant_name,region_name=os_region_name)
#    glance_endpoint = keystone.service_catalog.url_for(service_type='image',
#                                                       endpoint_type='publicURL')
#    glance = glclient.Client(endpoint=glance_endpoint,token=keystone.auth_token)
#    try:
#        glance_output=glance.images.list(image_id=id)
#    except Exception as e:
#        print("Error %s" % e.message)
#        #os._exit(1)
#    return glance_output

def glanceImageCreate(name, description,distro,url):
    from glanceclient.v1 import client as glclient
    from keystoneclient import session
    from keystoneclient.v2_0 import client as keystone_client
    import  logging
    from glanceclient.common import http
    import re
    import pprint

    logging.basicConfig()
    keystone = keystone_client.Client(auth_url=keystone_authtoken_auth_url,
                                      username=keystone_authtoken_user,
                                      password=keystone_authtoken_user_password,
                                      tenant_name=keystone_authtoken_user_tenant_name,
                                      region_name=os_region_name)
    glance_endpoint = keystone.service_catalog.url_for(service_type='image',
                                                       endpoint_type='publicURL')
    glance = glclient.Client(endpoint=glance_endpoint,token=keystone.auth_token)
    exit_status=0
    imagefile=url+distro+'.raw'
    try:
        with open(imagefile) as fimg:
            image = glance.images.create(
                name=name,is_public=True,
                disk_format='raw',
                container_format='bare',
                data=fimg,properties={
                    'description': description,
                })
    except Exception as e:
        print("Error open image file %s" % e.message)
        exit_status=1
    return exit_status


def glanceImageUpdate(id, description_old,name,today):
    from glanceclient.v2 import client as glclient
    from keystoneclient import session
    from keystoneclient.v2_0 import client as keystone_client
    import re
    import pprint
    update_status=0
    keystone = keystone_client.Client(
        auth_url=keystone_authtoken_auth_url,
        username=keystone_authtoken_user,
        password=keystone_authtoken_user_password,
        tenant_name=keystone_authtoken_user_tenant_name,
        region_name=os_region_name)
    glance_endpoint = keystone.service_catalog.url_for(
        service_type='image', endpoint_type='publicURL')
    glance = glclient.Client(endpoint=glance_endpoint,token=keystone.auth_token)
    try:
        name=name+"-"+str(today)
        glance_output=glance.images.update(image_id=id,
                                           name=name,
                                           visibility="private",
                                           description=description_old)
    except Exception as e:
        print("Error in glance image update %s" % e.message)
        update_status=1
        #os._exit(1)

    #glance_command.append('>&  /tmp/GLANCE_UPDATE_DEBUG')
    return update_status

def fileCreate(name,message):

    file = open(name, 'w+')
    file.write(message)
    file.close()

def Exec(region,distros,descriptionsMapLong,engines_names):

    import os.path
    import re

    exit_fin=0
    existingImagesIDs=[]
    existingImagesIdsFinal={}
    for i in distros:
        existingImagesIdsFinal[i]=[]
        engines_name=engines_names[i]
        #We identify the currently existing official Public images of a specific distro (e.g. ubuntu)
        existingImages=glanceImagesIds(engines_name)
        for j in existingImages: #j is the image id like 83c789a5-d834-4101-8256-3423fe579313
            if existingImages[j]['visibility'] == 'public' \
               and existingImages[j]['owner'].encode('UTF8') == os_tenant_id:
                existingImagesIdsFinal[i].append(j)
    for i in distros:
        if not len(existingImagesIdsFinal[i]) > 1:
            #error conditions for the distros.raw
            if not   os.path.isfile(url+str(i)+'_ERROR'):
                engines_name=engines_names[i]
                description=descriptionsMapLong[i]
                #creation of the new image
                exit_status=glanceImageCreate(engines_name,description,i,url)
                #print "glanceImageCreate %s with exit status %d" % (i,exit_status)
                #Moving away the old image with update (if creation of new one succeded)
                #print "%s %d" % (existingImagesIdsFinal[i],len(existingImagesIdsFinal[i]))
                if exit_status == 0 and len(existingImagesIdsFinal[i]) == 1:
                    update_status=glanceImageUpdate(existingImagesIdsFinal[i][0],
                                                    description_old,
                                                    engines_name,
                                                    str(today))
                    #print "glanceImageUpdate %s with exit status %d" % (i,update_status)
                    #check if the moving away of the old image succeded
                    if  update_status != 0:
                        fileCreate('/tmp/ERROR_UPDATE_IMAGES_GLANCE_' \
                                   + engines_name+'_'+region,
                                   "Exit status="+str(update_status) + " " \
                                   "Id="+str(existingImagesIdsFinal).strip('[]') + " " \
                                   "Description="+description_old + " " \
                                   "Name="+engines_name + " " \
                                   "Date="+str(today))
                        exit_fin=1
                    else:
                        fileCreate('/tmp/ERROR_CREATION_IMAGES_GLANCE_' \
                                   + engines_name+'_'+region,
                                   "Exit status="+str(exit_status) + " " \
                                   "Description="+description_old + " " \
                                   "Name="+engines_name + " " \
                                   "Date="+str(today))
                        exit_fin=1
        else:
            # if counterTest condition trigers an error, then we
            # report it as a touch file
            fileCreate('/tmp/ERROR_TOO_MANY_IMAGES_GLANCE_' \
                       +engines_name + '_' + i + '_' + region,
                       "")
            print("ERROR_TOO_MANY_IMAGES_GLANCE",counterTest[i])
            exit_fin=1

    sys.exit(exit_fin)


if __name__ == "__main__":
    sys.exit(main())
