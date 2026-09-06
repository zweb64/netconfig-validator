from netmiko import ConnectHandler
from getpass import getpass
from src.parser import get_vlans, get_telnet_state, get_ssh_state
from src.validator import (
    validate_ssh_state,
    validate_telnet_state,
    validate_vlans,
)
def get_running_config(host, username, password, secret):
    device = {
        "device_type": "ubiquiti_edgeswitch",
        "host": host,
        "username": username,
        "password": password,
        "secret": secret,
        }

    connection = ConnectHandler(**device)

    config_text = connection.send_command("show running-config")
    config_ssh = connection.send_command("show ip ssh")

    return {
    "running_config": config_text,
    "ssh_config": config_ssh,
    }


if __name__ == "__main__":
    host = input("host: ")
    username = input("username:")
    password = getpass("password:")
    secret = getpass("enable password:")


    device_data = get_running_config(host, username, password, secret)

    config_text = device_data["running_config"]
    config_ssh = device_data["ssh_config"]
    vlans = get_vlans(config_text)
    telnet_state = get_telnet_state(config_text)
    ssh_state = get_ssh_state(config_ssh)
    ssh_validation = validate_ssh_state(ssh_state)
    telnet_validation = validate_telnet_state(telnet_state)
    expected_vlans = [10, 20]
    vlan_validation = validate_vlans(vlans, expected_vlans)

    print("VLANs:", vlans)
    print("Telnet:", telnet_state)
    print("SSH:", ssh_state)
    print(ssh_validation)
    print(telnet_validation)
    print(vlan_validation)