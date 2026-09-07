# v1.0.0 Release Checklist

- [ ] `README.md` added
- [ ] `.gitignore` updated
- [ ] `pyproject.toml` verified
- [ ] CI workflow installs `.[dev]`
- [ ] Release workflow added
- [ ] `python -m pytest` -> 24 passed
- [ ] `python -m build` succeeds
- [ ] Wheel installs successfully in a fresh virtual environment
- [ ] `netconfig-validator` launches from the clean environment
- [ ] No credentials or local artifacts are tracked
- [ ] Changes committed on `prepare-v1-release`
- [ ] Pull request opened
- [ ] CI passes on pull request
- [ ] Pull request merged to `main`
- [ ] CI passes on `main`
- [ ] `v1.0.0` tag created and pushed
- [ ] GitHub Release created automatically
