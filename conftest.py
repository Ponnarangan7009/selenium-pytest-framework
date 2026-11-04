from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    browser = webdriver.Chrome(options=options)
    try:
        yield browser
    finally:
        browser.quit()

@pytest.fixture()
def safari_driver():
    browser = webdriver.Safari()
    try:
        yield browser
    finally:
        browser.quit()
