# NetConfig Validator

A Python network configuration validation tool that connects to supported network devices over SSH, collects configuration and operational state, parses the returned CLI output, and validates the device against defined policy.

## v1 Features

- Connects to Ubiquiti EdgeSwitch devices over SSH using Netmiko
- Collects running configuration and SSH state
- Validates required VLANs
- Validates expected SSH state
- Validates expected Telnet state
- Handles authentication failures and connection timeouts
- Produces structured PASS / FAIL / UNKNOWN / ERROR results
- Includes automated pytest coverage
- Runs in GitHub Actions CI
- Installs as a Python package with the `netconfig-validator` CLI command

## Supported Platform

v1 is built and tested around:

- Ubiquiti EdgeSwitch
- Netmiko device type: `ubiquiti_edgeswitch`
- EdgeSwitch 1.9.x-style CLI output

Additional vendors and device families are planned for future versions.

## Requirements

- Python 3.11 or newer
- Network reachability to the target switch
- Valid SSH credentials
- SSH enabled on the target device

## Installation

Clone the repository:

```powershell
git clone https://github.com/zweb64/netconfig-validator.git
cd netconfig-validator
```

Install the application:

```powershell
python -m pip install .
```

For development:

```powershell
python -m pip install -e ".[dev]"
```

## Usage

After installation:

```powershell
netconfig-validator
```

You can also run it directly from the repository:

```powershell
python -m src.cli
```

The CLI prompts for:

- Host/IP address
- Username
- Password
- Enable secret

Passwords and enable secrets are entered using Python's `getpass` and are not displayed in the terminal.

## Example Output

```text
Network Configuration Validator
================================
Device: 192.168.1.48

[PASS] SSH Enabled
       Expected: Enabled
       Actual:   Enabled

[FAIL] Telnet Disabled
       Expected: Disabled
       Actual:   Enabled

[PASS] Required VLANs Present
       Expected: [10, 20]
       Actual:   [10, 20]
       Missing:  []
       Unexpected: []

--------------------------------
Summary: 2 PASS | 1 FAIL | 0 UNKNOWN | 0 ERROR
```

## Validation Policy

The expected configuration policy is defined in:

```text
src/rules.py
```

Example:

```python
EXPECTED_VLANS = [10, 20]
EXPECTED_SSH_STATE = "Enabled"
EXPECTED_TELNET_STATE = "Disabled"
```

The validator compares collected device state against these expected values.

## Project Architecture

```text
User input / credentials
        |
        v
   connector.py
        |
        v
   raw CLI output
        |
        v
     parser.py
        |
        v
 normalized state
        |
        v
   validator.py
        |
        v
      cli.py
```

Responsibilities are intentionally separated:

- `connector.py` handles device connectivity and command collection.
- `parser.py` converts raw CLI output into normalized values.
- `validator.py` compares normalized state against policy.
- `rules.py` defines expected configuration.
- `cli.py` coordinates collection, validation, and reporting.

## Tests

Run the test suite with:

```powershell
python -m pytest
```

The v1 test suite covers parser and validator behavior, including alternate SSH and Telnet policy states.

## Continuous Integration

GitHub Actions runs the test suite automatically for:

- Pushes to `main`
- Pull requests targeting `main`

The CI workflow installs the project and development dependencies from `pyproject.toml` before executing pytest.

## Building a Release

Install the build package:

```powershell
python -m pip install build
```

Build the source distribution and wheel:

```powershell
python -m build
```

Release artifacts are created in:

```text
dist/
```

Tags matching `v*` trigger the GitHub Actions release workflow, which builds the package and creates a GitHub Release containing the generated artifacts.

## Security Notes

- Credentials are prompted at runtime.
- Passwords and enable secrets are not hardcoded in the project.
- Do not commit credentials, device secrets, or production configuration containing sensitive information.
- Validate the tool in a lab environment before using it against production infrastructure.

## Roadmap

Potential future development includes:

- Windows GUI
- Standalone Windows executables
- NSIS installer
- Multiple vendor platforms
- Policy profiles
- Batch device validation
- Exportable validation reports

## Version

Current release target: **v1.0.0**
