from netmiko import (
    ConnectHandler,
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
)
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

    try: 
        connection = ConnectHandler(**device)
    except NetmikoAuthenticationException:
        return None
    except NetmikoTimeoutException:
        return "TIMEOUT"

    config_text = connection.send_command("show running-config")
    config_ssh = connection.send_command("show ip ssh")

    return {
    "running_config": config_text,
    "ssh_config": config_ssh,
        }


