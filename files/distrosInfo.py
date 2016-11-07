global distrosMap, descriptionsMap, description_old

descriptionText="Please refer to http://help.switch.ch/engines/documentation/switch-official-images for further information"
description_old="Deprecated, please use the most recent version, with property Public"

distrosMap={}

#template: distrosMap["distrosKey"]=[diskimage-builder target e.g. debian, image name, DIB_DISTRIBUTION_MIRROR,DIB_RELEASE,PATH,DESCRIPTION]

distrosMap["centos_7"] = {
  	"target":"centos7",
  	"image_name":"CentOS 7.2 (SWITCHengines)",
  	"dib_distribution_mirror":"http://mirror.switch.ch/ftp/mirror/centos/",
  	"dib_release":"",
  	"path":"/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/",
  	"os_flavor":"centos",
	"default_user":"centos",
    "os_version":"7.2",
    "requires_rdp":"false",
    "requires_ssh":"true"
}

distrosMap["debian_jessie"] = {
  	"target":"debian",
  	"image_name":"Debian Jessie 8.2 (SWITCHengines)",
  	"dib_distribution_mirror":"http://ftp.ch.debian.org/debian/",
  	"dib_release":"Jessie",
	"path":"/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/",
  	"os_flavor":"debian",
	"default_user":"debian",
    "os_version":"Jessie 8.6",
    "requires_rdp":"false",
    "requires_ssh":"true"
}

distrosMap["debian_wheezy"] = {
  	"target":"debian",
  	"image_name":"Debian Wheezy 7.11 (SWITCHengines)",
  	"dib_distribution_mirror":"http://ftp.ch.debian.org/debian/",
  	"dib_release":"Wheezy",
	"path":"/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/",
  	"os_flavor":"debian",
	"default_user":"debian",
    "os_version":"Wheezy 7.11",
    "requires_rdp":"false",
    "requires_ssh":"true"
}

distrosMap["fedora_22"] = {
  	"target":"fedora",
  	"image_name":"Fedora release 22 (SWITCHengines)",
  	"dib_distribution_mirror":"http://mirror.switch.ch/ftp/mirror/fedora/linux",
  	"dib_release":"",
  	"path":"/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/",
  	"os_flavor":"fedora",
	"default_user":"fedora",
    "os_version":"22",
    "requires_rdp":"false",
    "requires_ssh":"true"
}

distrosMap["ubuntu_trusty"] = {
  	"target":"ubuntu",
  	"image_name":"Ubuntu Trusty 14.04 (SWITCHengines)",
  	"dib_distribution_mirror":"http://ch.archive.ubuntu.com/ubuntu",
  	"dib_release":"",
  	"path":"/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/",
  	"os_flavor":"ubuntu",
	"default_user":"ubuntu",
    "os_version":"Trusty 14.04",
    "requires_rdp":"false", 
    "requires_ssh":"true"
}

distrosMap["ubuntu_xenial"] = {
  	"target" : "ubuntu",
  	"image_name": "Ubuntu Xenial 16.04 (SWITCHengines)",
  	"dib_distribution_mirror":"http://ch.archive.ubuntu.com/ubuntu",
  	"dib_release":"",
  	"path":"/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/",
  	"os_flavor":"ubuntu",
	"default_user":"ubuntu",
    "os_version":"Xenial 16.04",
    "requires_rdp":"false", 
    "requires_ssh":"true"
}

distrosMap["rstudio"] = {
  	"target":"ubuntu",
  	"image_name":"RStudio Appliance (SWITCHengines)",
  	"dib_distribution_mirror":"http://ch.archive.ubuntu.com/ubuntu",
  	"dib_release":"",
  	"path":"/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/",
  	"os_flavor":"ubuntu",
	"default_user":"ubuntu",
    "os_version":"Trusty 14.04",
    "requires_rdp":"false", 
    "requires_ssh":"true"
}

distrosMap["zeppelin"] = {
  	"target":"ubuntu",
  	"image_name":"Spark Zeppelin (SWITCHengines)",
  	"dib_distribution_mirror":"http://ch.archive.ubuntu.com/ubuntu",
  	"dib_release":"",
  	"path":"/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/",
  	"os_flavor":"ubuntu",
	"default_user":"ubuntu",
    "os_version":"Trusty 14.04",
    "requires_rdp":"false", 
    "requires_ssh":"true"
}
