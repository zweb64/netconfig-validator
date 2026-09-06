from src.validator import (
    validate_ssh_state,
    validate_telnet_state,
    validate_vlans,
)


def test_validate_ssh_state_enabled():
    result = validate_ssh_state("Enabled")

    assert result == {
        "rule": "SSH Enabled",
        "status": "PASS",
        "expected": "Enabled",
        "actual": "Enabled"
    }


def test_validate_ssh_state_disabled():
    result = validate_ssh_state("Disabled")

    assert result == {
        "rule": "SSH Enabled",
        "status": "FAIL",
        "expected": "Enabled",
        "actual": "Disabled"
    }


def test_validate_ssh_state_unknown():
    result = validate_ssh_state("Unknown")

    assert result == {
        "rule": "SSH Enabled",
        "status": "UNKNOWN",
        "expected": "Enabled",
        "actual": "Unknown"
    }


def test_validate_ssh_state_invalid():
    result = validate_ssh_state("Banana")

    assert result == {
        "rule": "SSH Enabled",
        "status": "ERROR",
        "expected": "Enabled",
        "actual": "Banana"
    }


def test_validate_telnet_state_disabled():
    result = validate_telnet_state("Disabled")

    assert result == {
        "rule": "Telnet Disabled",
        "status": "PASS",
        "expected": "Disabled",
        "actual": "Disabled"
    }


def test_validate_telnet_state_enabled():
    result = validate_telnet_state("Enabled")

    assert result == {
        "rule": "Telnet Disabled",
        "status": "FAIL",
        "expected": "Disabled",
        "actual": "Enabled"
    }


def test_validate_telnet_state_invalid():
    result = validate_telnet_state("Banana")

    assert result == {
        "rule": "Telnet Disabled",
        "status": "ERROR",
        "expected": "Disabled",
        "actual": "Banana"
    }

def test_validate_vlans_exact_match():
    result = validate_vlans([10, 20], [10, 20])

    assert result == {
        "rule": "Required VLANs Present",
        "status": "PASS",
        "expected": [10, 20],
        "actual": [10, 20],
        "missing": [],
        "unexpected": []
    }


def test_validate_vlans_unexpected_vlan():
    result = validate_vlans([10, 20, 30], [10, 20])

    assert result == {
        "rule": "Required VLANs Present",
        "status": "PASS",
        "expected": [10, 20],
        "actual": [10, 20, 30],
        "missing": [],
        "unexpected": [30]
    }


def test_validate_vlans_missing_vlan():
    result = validate_vlans([10], [10, 20])

    assert result == {
        "rule": "Required VLANs Present",
        "status": "FAIL",
        "expected": [10, 20],
        "actual": [10],
        "missing": [20],
        "unexpected": []
    }


def test_validate_vlans_missing_and_unexpected():
    result = validate_vlans([10, 30], [10, 20])

    assert result == {
        "rule": "Required VLANs Present",
        "status": "FAIL",
        "expected": [10, 20],
        "actual": [10, 30],
        "missing": [20],
        "unexpected": [30]
    }