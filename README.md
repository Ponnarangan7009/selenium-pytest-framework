# Selenium Pytest Framework

A small, learning-oriented UI test framework for the [SauceDemo](https://www.saucedemo.com/) practice site. It uses pytest for test cases and fixtures, Selenium WebDriver for browser control, and page objects to keep selectors and browser actions together.

## Project structure

```text
.
├── conftest.py             # Shared browser fixtures
├── pages/                  # Page objects and page actions
├── util/                   # Shared Selenium waits and browser actions
├── tests/                  # Login, cart, and checkout scenarios
├── pytest.ini              # Test discovery and markers
└── requirements.txt        # Python dependencies
```

## Setup

Use Python 3.10 or newer. Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate      # Windows PowerShell
python -m pip install -r requirements.txt
```

Selenium Manager can locate or download a compatible Chrome driver when Chrome is installed. The tests need an internet connection to reach SauceDemo. The `safari_driver` fixture is available for Safari runs on macOS, but the current tests use Chrome.

## Run tests

```bash
pytest
```

Run only the fast smoke checks or the broader regression checks:

```bash
pytest -m smoke
pytest -m regression
```

## Test accounts

The tests use the public SauceDemo practice accounts `standard_user`, `error_user`, and `locked_out_user`, with the site's sample password `secret_sauce`. These are demo credentials, not personal account credentials.
