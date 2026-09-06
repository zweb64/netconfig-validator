def validate_ssh_state(ssh_state):
    if ssh_state == "Enabled":
        return {
            "rule": "SSH Enabled",
            "status": "PASS",
            "expected": "Enabled",
            "actual": ssh_state
    }
    if ssh_state == "Disabled":
        return {
            "rule": "SSH Enabled",
            "status": "FAIL",
            "expected": "Enabled",
            "actual": ssh_state
    }
    if ssh_state == "Unknown":
        return {
            "rule": "SSH Enabled",
            "status": "UNKNOWN",
            "expected": "Enabled",
            "actual": ssh_state
    }
    else:
        return {
            "rule": "SSH Enabled",
            "status": "ERROR",
            "expected": "Enabled",
            "actual": ssh_state
        }
        
def validate_telnet_state(telnet_state):
    if telnet_state == "Disabled":
        return {
            "rule": "Telnet Disabled",
            "status": "PASS",
            "expected": "Disabled",
            "actual": telnet_state
        }
    if telnet_state == "Enabled":
        return {
            "rule": "Telnet Disabled",
            "status": "FAIL",
            "expected": "Disabled",
            "actual": telnet_state
        }
    else:
        return {
            "rule": "Telnet Disabled",
            "status": "ERROR",
            "expected": "Disabled",
            "actual": telnet_state
        }

def validate_vlans(actual_vlans, expected_vlans):
    actual_vlans = set(actual_vlans)
    expected_vlans = set(expected_vlans)
    missing_vlan = expected_vlans - actual_vlans
    unexpected_vlan = actual_vlans - expected_vlans
    if not missing_vlan:
        return {
        "rule": "Required VLANs Present",
        "status": "PASS",
        "expected": sorted(expected_vlans),
        "actual": sorted(actual_vlans),
        "missing": sorted(missing_vlan),
        "unexpected": sorted(unexpected_vlan)
        }
    else:
        return {
        "rule": "Required VLANs Present",
        "status": "FAIL",
        "expected": sorted(expected_vlans),
        "actual": sorted(actual_vlans),
        "missing": sorted(missing_vlan),
        "unexpected": sorted(unexpected_vlan)
        }