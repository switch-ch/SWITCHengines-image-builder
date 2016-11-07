global distrosMap, descriptionsMap, description_old

descriptionText = "Please refer to http://help.switch.ch/engines/documentation/switch-official-images for further information"

distrosMap = {}

# template: distrosMap["distrosKey"]=[diskimage-builder target e.g. debian, image name, DIB_DISTRIBUTION_MIRROR,DIB_RELEASE,PATH,DESCRIPTION]

distrosMap["centos7"] = {
	"target": "centos7",
	"image_name": "CentOS 7.2 (SWITCHengines)",
	"os_flavor": "centos",
	"default_user": "centos",
	"os_version": "7.2",
	"requires_rdp": "false",
	"requires_ssh": "true",
    "min_ram": "512"
   
}

distrosMap["debianJessie"] = {
	"target": "debian",
	"image_name": "Debian Jessie 8.6 (SWITCHengines)",
	"os_flavor": "debian",
	"default_user": "debian",
	"os_version": "Jessie 8.6",
	"requires_rdp": "false",
	"requires_ssh": "true",
    "min_ram": "512"
}

distrosMap["debianWheezy"] = {
	"target": "debian",
	"image_name": "Debian Wheezy 7.11 (SWITCHengines)",
	"os_flavor": "debian",
	"default_user": "debian",
	"os_version": "Wheezy 7.11",
	"requires_rdp": "false",
	"requires_ssh": "true",
    "min_ram": "512"
}

distrosMap["fedora"] = {
	"target": "fedora",
	"image_name": "Fedora release 22 (SWITCHengines)",
	"os_flavor": "fedora",
	"default_user": "fedora",
	"os_version": "22",
	"requires_rdp": "false",
	"requires_ssh": "true",
    "min_ram": "512"
}

distrosMap["ubuntu"] = {
	"target": "ubuntu",
	"image_name": "Ubuntu Trusty 14.04 (SWITCHengines)",
	"os_flavor": "ubuntu",
	"default_user": "ubuntu",
	"os_version": "Trusty 14.04",
	"requires_rdp": "false",
	"requires_ssh": "true",
    "min_ram": "512"
}

distrosMap["ubuntuxenial"] = {
	"target": "ubuntu",
	"image_name": "Ubuntu Xenial 16.04 (SWITCHengines)",
	"os_flavor": "ubuntu",
	"default_user": "ubuntu",
	"os_version": "Xenial 16.04",
	"requires_rdp": "false",
	"requires_ssh": "true",
    "min_ram": "512"
}

distrosMap["rstudio"] = {
	"target": "ubuntu",
	"image_name": "RStudio Appliance (SWITCHengines)",
	"os_flavor": "ubuntu",
	"default_user": "ubuntu",
	#"os_version": "Trusty 14.04", Dont tag as Trusty, breaks Quick UI
	"os_version": "None", 
	"requires_rdp": "false",
	"requires_ssh": "true",
    "min_ram": "4096"
}


distrosMap["zeppelin"] = {
	"target": "ubuntu",
	"image_name": "Spark Zeppelin (SWITCHengines)",
	"os_flavor": "ubuntu",
	"default_user": "ubuntu",
	#"os_version": "Trusty 14.04", #Dont tag as Trusty, breaks QuickUI
	"os_version": "None", 
	"requires_rdp": "false",
	"requires_ssh": "true",
    "min_ram": "8192"
}
