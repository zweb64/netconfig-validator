from getpass import getpass



from src.connector import get_running_config

from src.parser import get_vlans, get_telnet_state, get_ssh_state

from src.validator import validate_vlans, validate_ssh_state, validate_telnet_state

from src.rules import EXPECTED_VLANS, EXPECTED_SSH_STATE, EXPECTED_TELNET_STATE

def print_validation_results(result):
    status = result["status"]
    rule = result["rule"]
    expected = result["expected"]
    actual = result["actual"]
    print(f"{status} {rule}")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    if "missing" in result:
        missing_vlan = result["missing"]
        print(f"Missing: {missing_vlan}")
    if "unexpected" in result:
        unexpected_vlan = result["unexpected"]
        print(f"Unexpected: {unexpected_vlan}")
    



if __name__ == "__main__":
    host = input("host: ")
    username = input("username:")
    password = getpass("password:")
    secret = getpass("enable secret:")
    while True:
        username = input("username:")
        password = getpass("password:")
        secret = getpass("secret:")


        device_data = get_running_config(host, username, password, secret)


        if device_data is None:
            print("Authentication failed. Please try again.")
            username = input("username:")
            password = getpass("password:")
            secret = getpass("enable secret:")
        if device_data == "TIMEOUT":
            print("Unable to reach device. Please try another host.")
            host = input("host: ")

        if device_data is not None and device_data != "TIMEOUT":
            break
    
    
    
    
    config_text = device_data["running_config"]
    config_ssh = device_data["ssh_config"]
    vlans = get_vlans(config_text)
    telnet_state = get_telnet_state(config_text)
    ssh_state = get_ssh_state(config_ssh)
    ssh_validation = validate_ssh_state(ssh_state, EXPECTED_SSH_STATE)
    telnet_validation = validate_telnet_state(telnet_state, EXPECTED_TELNET_STATE)

    vlan_validation = validate_vlans(vlans, EXPECTED_VLANS)

    print_validation_results(ssh_validation)
    print()
    print_validation_results(telnet_validation)
    print()
    print_validation_results(vlan_validation)
