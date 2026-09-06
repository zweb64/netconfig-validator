
def load_config_file():
    with open("examples/ubiquiti_edgeswitch_base.conf") as load_config:
        config_text = load_config.read()
        return config_text

def get_system_description(config_text):
    for line in config_text.splitlines():
        if line.startswith("!System Description"):
            config_name = line.replace("!System Description", "")
            config_name = config_name.strip()
            config_name = config_name.strip('"')
            return config_name


def get_software_version(config_text):
    for line in config_text.splitlines():
        if line.startswith("!System Software Version"):
            software_version = line.replace("!System Software Version", "")
            software_version = software_version.strip()
            software_version = software_version.strip('"')
            return software_version


def get_system_uptime(config_text):
    for line in config_text.splitlines():
        if line.startswith("!System Up Time"):
            system_uptime = line.replace("!System Up Time", "")
            system_uptime = system_uptime.strip()
            system_uptime = system_uptime.strip('"')
            return system_uptime


def get_additional_packages_list(config_text):
    additional_packages_list = []
    for line in config_text.splitlines():
        if line.startswith("!Additional Packages"):
            additional_packages = line.replace("!Additional Packages", "")
            additional_packages = additional_packages.strip()
            additional_packages = additional_packages.split(",")
            for item in additional_packages:
               item = item.strip()
               if item != "":
                additional_packages_list.append(item)
            return additional_packages_list


def get_vlans(config_text):
    in_vlan_database = False
    vlans_list = []
    for line in config_text.splitlines():
        if line.strip() == "vlan database":
            in_vlan_database = True
        if in_vlan_database and line.startswith("vlan ") and line.strip() != "vlan database":
            vlans = line.replace("vlan", "")
            vlans = vlans.strip()
            vlans = vlans.split(",")
            for item in vlans:
                item = item.strip()
                if item != "":
                    item = int(item)
                    vlans_list.append(item)
        if line.strip() == "exit":
            in_vlan_database = False
    return vlans_list


def get_telnet_state(config_text):
    for line in config_text.splitlines():
        if line.strip() == "ip telnet server enable":
            return "Enabled"
    return "Disabled"
            
                
def get_ssh_state(config_ssh):
    for line in config_ssh.splitlines():
        if line.strip().startswith("Administrative Mode:"):
            if "Enabled" in line: 
                return "Enabled"
            if "Disabled" in line:
                return "Disabled"
            else:
                return "Unknown"
    return "Unknown"

if __name__ == "__main__":
    # load config
    # print results
    
    config_text = load_config_file()
    print(get_system_description(config_text))
    print(get_software_version(config_text))
    print(get_system_uptime(config_text))
    print(get_additional_packages_list(config_text))
    print(get_vlans(config_text))
    print(get_telnet_state(config_text))