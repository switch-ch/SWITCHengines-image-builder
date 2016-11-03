global distrosMap, descriptionsMap, description_old

descriptionText="Please refer to http://help.switch.ch/engines/documentation/switch-official-images for further information"
description_old="Deprecated, please use the most recent version, with property Public"

distrosMap={}

#template: distrosMap["distrosKey"]=[diskimage-builder target e.g. debian, image name, DIB_DISTRIBUTION_MIRROR,DIB_RELEASE,PATH,DESCRIPTION]

distrosMap["centos7"]=["centos7","CentOS 7.1 (SWITCHengines)","http://mirror.switch.ch/ftp/mirror/centos/","","/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/","User: centos . "+descriptionText]

distrosMap["debianWheezy"]=["debian","Debian Wheezy 7.8 (SWITCHengines)","http://ftp.ch.debian.org/debian/", "wheezy", "/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/","User: debian . "+ descriptionText]

distrosMap["ubuntu"]=["ubuntu","Ubuntu Trusty 14.04 (SWITCHengines)","http://ch.archive.ubuntu.com/ubuntu","","/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/","User: ubuntu . "+descriptionText]

distrosMap["fedora"]=["fedora","Fedora release 20 (SWITCHengines)", "http://mirror.switch.ch/ftp/mirror/fedora/linux","","/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/","User: fedora . "+descriptionText]

distrosMap["debianJessie"]=["debian","Debian Jessie 8.1 (SWITCHengines)","http://ftp.ch.debian.org/debian/", "Jessie", "/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/","User: debian . "+ descriptionText]

distrosMap["rstudio"]=["ubuntu","RStudio Appliance (SWITCHengines)","http://ch.archive.ubuntu.com/ubuntu","","/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/","User: ubuntu . "+descriptionText]

distrosMap["ubuntuxenial"]=["ubuntu","Ubuntu Xenial 16.04 (SWITCHengines)","http://ch.archive.ubuntu.com/ubuntu","","/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/","User: ubuntu . "+descriptionText]

distrosMap["zeppelin"]=["ubuntu","Spark and Zeppelin Appliance (SWITCHengines)","http://ch.archive.ubuntu.com/ubuntu","","/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin:/home/ubuntu/diskimage-builder/bin:/home/ubuntu/dib-utils/bin/","User: ubuntu . "+descriptionText]
