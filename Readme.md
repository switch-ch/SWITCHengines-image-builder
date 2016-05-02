# Readme

## Create a Ubuntu VM in Openstack to run diskimage-builder

Create your config file:

`
cp vars.yaml.template vars.yaml
`

Source your openstack config:

`
source ~/openrc
`

Run the playbook

`
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook main.yaml
`

## Build the images

Now you can login to the instance and use the ./SWITCHengines-create-images.sh script

You can check the progress of the script with the logfiles produced in the `/tmp` folder.

When everthing is OKAY, you will find the images in
`
/usr/share/nginx/html/images/
`

The images are served with nginx over http at the URL http://ip.domain/images/

## Upload images to glance

We also provide a tool to upload the new created images to glance: `SWITCHengines-image-uploader.py`

You will need openstack admin rights to run this tool.

The new images will be uploaded as public.

This tool is meant to refresh existing images. It will change the name of old version of the images already present, and disable them from being public. The old images will have in the name the timestamp of when they have been deactivated. The users will not be able to start new VMs using the old images. However note that old images cannot be deleted from glance, because there are possibly cinder volumes and nova ephemeral volumes depending from the old glance images. This is a consequence of the CoW features of rbd.
