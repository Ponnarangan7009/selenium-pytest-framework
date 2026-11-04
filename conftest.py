from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture()
def safari_driver():
    browser = webdriver.Safari()
    yield browser
    browser.quit()