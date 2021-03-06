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
        "os_flavor_name": "CentOS (SWITCHengines)",
        "default_user": "centos",
        "os_version": "7.3",
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
        "os_flavor_name": "Debian (SWITCHengines)",
        "default_user": "debian",
        "os_version": "Jessie 8.8",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["debian_stretch"] = {
    "image_raw_source": "debianStretch.raw",
    "image_name": "Debian Stretch 9 (SWITCHengines)",
    "image_min_ram": "512",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'debian'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "debian",
        "os_flavor_name": "Debian (SWITCHengines)",
        "default_user": "debian",
        "os_version": "Stretch 9",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["fedora"] = {
    "image_raw_source": "fedora.raw",
    "image_name": "Fedora 25 (SWITCHengines)",
    "image_min_ram": "512",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'fedora'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "fedora",
        "os_flavor_name": "Fedora (SWITCHengines)",
        "default_user": "fedora",
        "os_version": "25",
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
        "os_flavor_name": "Ubuntu (SWITCHengines)",
        "default_user": "ubuntu",
        "os_version": "Trusty 14.04",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}

images_info["ubuntu_gpu"] = {
    "image_raw_source": "ubuntugpu.raw",
    "image_name": "Ubuntu Xenial with GPU support (SWITCHengines)",
    "image_min_ram": "2048",
    "image_min_disk": "auto",
    "image_properties": {
        "description": "Username: 'ubuntu'. See http://help.switch.ch/engines/documentation/switch-official-images for further information",
        "hw_vif_multiqueue_enabled": "true",
        "os_flavor": "ubuntu",
        "os_flavor_name": "Ubuntu (SWITCHengines)",
        "default_user": "ubuntu",
        "os_version": "Xenial 16.04 (GPU)",
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
        "os_flavor_name": "Ubuntu (SWITCHengines)",
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
        "default_user": "ubuntu",
        "os_version": "Trusty 14.04",
        "requires_rdp": "false",
        "requires_ssh": "true"
    }
}
