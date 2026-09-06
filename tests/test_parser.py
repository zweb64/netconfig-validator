from src.parser import get_software_version, get_system_description, get_additional_packages_list, load_config_file,  get_system_uptime, get_vlans, get_telnet_state, get_ssh_state

import pytest

@pytest.fixture 
def config_text():
    return load_config_file()

def test_get_software_version(config_text):
    result = get_software_version(config_text)
    assert result == "1.9.2"


def test_get_system_description(config_text):
    result = get_system_description(config_text)
    assert result == "EdgeSwitch 48 500W, 1.9.2, Linux 3.6.5-03329b4a, 1.1.0.5102011"

def test_get_additional_packages(config_text):
    result = get_additional_packages_list(config_text)
    assert result == ["QOS", "IPv6 Management", "Routing"]

def test_get_additional_packages_handles_whitespace():
    config_text =  "!Additional Packages     QOS, IPv6 Management, Routing,"
    result = get_additional_packages_list(config_text)
    assert result == ["QOS", "IPv6 Management", "Routing"]

def test_get_system_uptime(config_text):
    result = get_system_uptime(config_text)
    assert result == "3 days 16 hrs 17 mins 55 secs"


def test_get_vlans(config_text):
    result = get_vlans(config_text)
    assert result == [10, 20, 30, 40]

def test_telnet_state_enabled(config_text):
    result = get_telnet_state(config_text)
    assert result == "Enabled"

def test_telnet_state_disabled():
    telnet_disabled_config = """
    line telnet
    exit
    """

    result = get_telnet_state(telnet_disabled_config)

    assert result is "Disabled"


def test_get_ssh_state_enabled():
    config_ssh = """
SSH Configuration

Administrative Mode: .......................... Enabled
SSH Port: ..................................... 22
Protocol Levels: .............................. Version 2
SSH Sessions Currently Active: ................ 1
Max SSH Sessions Allowed: ..................... 2
SSH Timeout: .................................. 5
Keys Present: ................................. DSA RSA
Key Generation In Progress: ................... None
"""

    assert get_ssh_state(config_ssh) == "Enabled"


def test_get_ssh_state_disabled():
    config_ssh = """
SSH Configuration

Administrative Mode: .......................... Disabled
SSH Port: ..................................... 22
Protocol Levels: .............................. Version 2
SSH Sessions Currently Active: ................ 0
Max SSH Sessions Allowed: ..................... 2
SSH Timeout: .................................. 5
Keys Present: ................................. DSA RSA
Key Generation In Progress: ................... None
"""

    assert get_ssh_state(config_ssh) == "Disabled"


def test_get_ssh_state_unknown():
    config_ssh = """
SSH Configuration

SSH Port: ..................................... 22
Protocol Levels: .............................. Version 2
"""

    assert get_ssh_state(config_ssh) == "Unknown"