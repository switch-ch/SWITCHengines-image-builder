# README

## Create a Ubuntu VM in Openstack to run diskimage-builder

Create your config file:

```
cp vars.yaml.template vars.yaml
```

Source your openstack config:

```
source ~/openrc
```

Run the playbook

```
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook main.yaml
```

## Build the images

Now you can login to the instance and use the
`./SWITCHengines-create-images.sh` script.

You can check the progress of the script with the logfiles produced in
the `/tmp` folder.

When everything is okay, you will find the images in
`/usr/share/nginx/html/images/`.

The images are served with nginx over http at the URL
http://ip.domain/images/

## Upload images to glance

We also provide a tool to upload the new created images to glance:

    SWITCHengines-images-uploader.py --all-regions

You will need openstack admin rights to run this tool.

The new images will be uploaded as public.

This tool is meant to refresh existing images.  It will change the
name of old version of the images already present, and make them
non-public.  The old images will have in the name the timestamp of
when they have been deactivated.  The users will not be able to start
new VMs using the old images.  However note that old images cannot be
deleted from Glance, because there are possibly Cinder volumes and
Nova ephemeral volumes depending on the old Glance images.  This is a
consequence of the CoW features of RBD.

## Testing images

Before upgrading to production you can manually make these checks
running the images privately on your tenant.

### login with ssh

 * Ubuntu: `ssh ubuntu@<FLOATING_IP>`
 * Debian: `ssh debian@<FLOATING_IP>`
 * Centos: `ssh centos@<FLOATING_IP>`

### check common commands

```bash
hostname
sudo su
init 6
```

Also check the hostname on the console.  Can also be checked via ssh
with: `cat /dev/vcs1`

Check  the file `/etc/apt/sources.list`

 * correct Release
 * security repo enabled
 * mirrors in Switzerland
 * Automatic Security Updates enabled?

In the file `/etc/apt/apt.conf.d/20auto-upgrades`
```
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
```

Can also be checked with something like:

`apt-config dump | grep Periodic`

In file `/etc/ntp.conf`, the pool should be in Switzerland

`ntpq -p`
