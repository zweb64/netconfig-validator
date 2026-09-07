def validate_ssh_state(ssh_state, expected_ssh_state):

    if ssh_state == expected_ssh_state:
        return {
            "rule": f"SSH {expected_ssh_state}",
            "status": "PASS",
            "expected": expected_ssh_state,
            "actual": ssh_state
        }

    if ssh_state in ["Enabled", "Disabled"]:
        return {
            "rule": f"SSH {expected_ssh_state}",
            "status": "FAIL",
            "expected": expected_ssh_state,
            "actual": ssh_state
        }

    if ssh_state == "Unknown":
        return {
            "rule": f"SSH {expected_ssh_state}",
            "status": "UNKNOWN",
            "expected": expected_ssh_state,
            "actual": ssh_state
        }

    else:
        return {
            "rule": f"SSH {expected_ssh_state}",
            "status": "ERROR",
            "expected": expected_ssh_state,
            "actual": ssh_state
        }


def validate_telnet_state(telnet_state, expected_telnet_state):

    if telnet_state == expected_telnet_state:
        return {
            "rule": f"Telnet {expected_telnet_state}",
            "status": "PASS",
            "expected": expected_telnet_state,
            "actual": telnet_state
        }

    if telnet_state in ["Enabled", "Disabled"]:
        return {
            "rule": f"Telnet {expected_telnet_state}",
            "status": "FAIL",
            "expected": expected_telnet_state,
            "actual": telnet_state
        }

    else:
        return {
            "rule": f"Telnet {expected_telnet_state}",
            "status": "ERROR",
            "expected": expected_telnet_state,
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