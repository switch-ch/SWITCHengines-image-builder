#
# images information config
#
description_deprecated = "DEPRECATED, please use the most recent public image"

images_info = {}

images_info["centos_7"] = {
    "image_raw_source": "centos7.raw",
    "image_name": "CentOS 7 (SWITCHengines)",
    "image_min_ram": "512",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'centos'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "centos",
        "default_user": "centos",
        "os_version": "7.2",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["debian_jessie"] = {
    "image_raw_source": "debianJessie.raw",
    "image_name": "Debian Jessie 8 (SWITCHengines)",
    "image_min_ram": "512",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'debian'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "debian",
        "default_user": "debian",
        "os_version": "Jessie 8.6",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["debian_wheezy"] = {
    "image_raw_source": "debianWheezy.raw",
    "image_name": "Debian Wheezy 7 (SWITCHengines)",
    "image_min_ram": "512",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'debian'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "debian",
        "default_user": "debian",
        "os_version": "Wheezy 7.11",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["fedora"] = {
    "image_raw_source": "fedora.raw",
    "image_name": "Fedora release 22 (SWITCHengines)",
    "image_min_ram": "512",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'fedora'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "fedora",
        "default_user": "fedora",
        "os_version": "22",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["ubuntu_trusty"] = {
    "image_raw_source": "ubuntu.raw",
    "image_name": "Ubuntu Trusty 14.04 (SWITCHengines)",
    "image_min_ram": "512",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'ubuntu'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "ubuntu",
        "default_user": "ubuntu",
        "os_version": "Trusty 14.04",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["ubuntu_xenial"] = {
    "image_raw_source": "ubuntuxenial.raw",
    "image_name": "Ubuntu Xenial 16.04 (SWITCHengines)",
    "image_min_ram": "512",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'ubuntu'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "ubuntu",
        "default_user": "ubuntu",
        "os_version": "Xenial 16.04",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["rstudio"] = {
    "image_raw_source": "rstudio.raw",
    "image_name": "RStudio Appliance (SWITCHengines)",
    "image_min_ram": "1024",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'ubuntu'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "ubuntu",
        "default_user": "ubuntu",
        "os_version": "Trusty 14.04",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["zeppelin"] = {
    "image_raw_source": "zeppelin.raw",
    "image_name": "Spark Zeppelin (SWITCHengines)",
    "image_min_ram": "4096",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'ubuntu'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "ubuntu",
        "default_user": "ubuntu",
        "os_version": "Trusty 14.04",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}
