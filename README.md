### Ride Management

Ride Management

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app ride_mng
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/ride_mng
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit



Task: Create a custom app named Ride Management. Duration: 1h	2
1. Create Customers Records (ERPNext):	2
2. Create 3 Items Records (ERPNext):	2
3. Create a new “Vehicle Ride” DocType with fields:	2
4. Create a new “Ride Add On” DocType with the fields:	2
5. Create a new “Ride Booking” DocType with the fields:	3
6. Export Fixtures:	3
7. Upload Ride Management App to GitHub:
