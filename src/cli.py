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
    print(f"[{status}] {rule}")
    print(f"       Expected: {expected}")
    print(f"       Actual:   {actual}")
    if "missing" in result:
        missing_vlan = result["missing"]
        print(f"Missing: {missing_vlan}")
    if "unexpected" in result:
        unexpected_vlan = result["unexpected"]
        print(f"Unexpected: {unexpected_vlan}")
    



def main():
    host = input("host: ")
    username = input("username:")
    password = getpass("password:")
    secret = getpass("enable secret:")
    while True:
        


        device_data = get_running_config(host, username, password, secret)


        if device_data is None:
            print("Authentication failed. Please try again.")
            username = input("username:")
            password = getpass("password:")
            secret = getpass("enable secret:")
        elif device_data == "TIMEOUT":
            print("Unable to reach device. Please try another host.")
            host = input("host: ")

        else:
            break
    
    
    
    
    config_text = device_data["running_config"]
    config_ssh = device_data["ssh_config"]
    vlans = get_vlans(config_text)
    telnet_state = get_telnet_state(config_text)
    ssh_state = get_ssh_state(config_ssh)
    ssh_validation = validate_ssh_state(ssh_state, EXPECTED_SSH_STATE)
    telnet_validation = validate_telnet_state(telnet_state, EXPECTED_TELNET_STATE)

    vlan_validation = validate_vlans(vlans, EXPECTED_VLANS)

    validation_results = [
    ssh_validation,
    telnet_validation,
    vlan_validation,
    ]

    print()
    print("Network Configuration Validator")
    print("================================")
    print(f"Device: {host}")
    print()

    for result in validation_results:
        print_validation_results(result)
        print()

    pass_count = 0
    fail_count = 0
    unknown_count = 0
    error_count = 0

    for result in validation_results:
        status = result["status"]

        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1
        elif status == "UNKNOWN":
            unknown_count += 1
        elif status == "ERROR":
            error_count += 1

    print("--------------------------------")
    print(
        f"Summary: {pass_count} PASS | "
        f"{fail_count} FAIL | "
        f"{unknown_count} UNKNOWN | "
        f"{error_count} ERROR"
    )

if __name__ == "__main__":
    main()