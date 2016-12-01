# README

## Create a Ubuntu VM in Openstack to run diskimage-builder

Create your config file:

    cp vars.yaml.template vars.yaml

and edit the `vars.yaml` file:

    vmname: images-builder-ansible
    image: Ubuntu Trusty 14.04 (SWITCHengines)
    flavor: m1.xlarge
    key_name: YOUR_KEY_NAME
    net_name: private
    ansible_user: ubuntu

Source your user OpenStack credentials:

    source ~/.openrc-user

Run the playbook

    export ANSIBLE_HOST_KEY_CHECKING=False
    ansible-playbook main.yaml

This will create an image builder VM, with all the required packages installed 
and configured.

## Build the images

Now you can login to the instance and use the script to build all the images:

    ./SWITCHengines-create-images.sh

Or you can build single distros using the `-d DISTRO` option, like:

    ./SWITCHengines-create-images.sh -d ubuntu -d centos7

The distro names are defined in the `distrosInfo` file

You can check the progress of the script with the logfiles produced in
the `/tmp` folder.

When everything is okay, you will find the images in
`/usr/share/nginx/html/images/`.

The images are served with nginx over http at the URL
http://ip.domain/images/

## Upload images to glance

**IMPORTANT**: You will need an OpenStack admin `openrc` file to run this tool.

Use the tool to upload the new created images to glance. To 
upload all the images in both region (S1/S2 or LS/ZH) use:

    source ~/.openrc-admin
    ./SWITCHengines-images-uploader.py -v --all-regions

Or to upload some selected distros use the `-d DISTRO` option, like:

    ./SWITCHengines-images-uploader.py  -v --all-regions -d ubuntu_trusty -d ubuntu_xenial

The distro names are defined in the `distrosInfo.py` file.

The new images will be uploaded as **public**.

This tool is meant to refresh existing images.  It will change the
name of old version of the images already present, and make them
**private**.  The archived images will have in the name the timestamp of
when they were initally created.  

The users will not be able to start new VMs using the old images.  
However note that old images cannot be deleted from Glance, 
because there are possibly Cinder volumes and Nova ephemeral volumes
depending on the old Glance images. This is a consequence of the 
CoW features of RBD.

## Testing images

Before upgrading to production you can manually make these checks
running the images privately on your tenant.

### login with ssh

 * Ubuntu: `ssh ubuntu@<FLOATING_IP>`
 * Debian: `ssh debian@<FLOATING_IP>`
 * Centos: `ssh centos@<FLOATING_IP>`
 * Fedora: `ssh fedora@<FLOATING_IP>`

### check common commands

    hostname
    sudo su
    init 6

Also check the hostname on the console.  Can also be checked via ssh
with: `cat /dev/vcs1`

Check  the file `/etc/apt/sources.list`

 * correct Release
 * security repo enabled
 * mirrors in Switzerland
 * Automatic Security Updates enabled?

In the file `/etc/apt/apt.conf.d/20auto-upgrades`

    APT::Periodic::Update-Package-Lists "1";
    APT::Periodic::Unattended-Upgrade "1";

Can also be checked with something like:

    apt-config dump | grep Periodic

In file `/etc/ntp.conf`, the pool should be in Switzerland

    ntpq -p
