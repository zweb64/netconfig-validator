from src.parser import get_software_version, get_system_description, get_additional_packages_list, load_config_file, get_system_uptime, get_vlans

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
    assert result == [10, 20]