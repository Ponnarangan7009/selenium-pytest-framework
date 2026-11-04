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
    yield browser
    browser.quit()

@pytest.fixture()
def safari_driver():
    browser = webdriver.Safari()
    yield browser
    browser.quit()
