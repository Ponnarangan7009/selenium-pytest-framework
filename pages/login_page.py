from selenium.webdriver.common.by import By
from util.selenium_helpers import click_when_ready, visible_element, wait_until


class LoginWebPage:
    """This class is for testing valid and invalid user"""

    URL = 'https://www.saucedemo.com/'
    LOGIN_USER = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
    SUBMIT = (By.CSS_SELECTOR, "input[id='login-button']")
    VALIDATOR = (By.CSS_SELECTOR, 'h3[role=alert]')
    VALIDATE_CART_ICON_PROPERTY = (By.CSS_SELECTOR, "a[class='shopping_cart_link']")

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        self.driver.get(self.URL)

    def enter_login_username(self, text):
        visible_element(self.driver, self.LOGIN_USER).send_keys(text)

    def enter_login_password(self, text):
        visible_element(self.driver, self.PASSWORD).send_keys(text)

    def submit_form(self):
        click_when_ready(self.driver, self.SUBMIT)

    def password_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def validate_user(self):
        def login_outcome(driver):
            error_messages = driver.find_elements(*self.VALIDATOR)
            if error_messages and error_messages[0].is_displayed():
                return "error", error_messages[0]

            cart_icons = driver.find_elements(*self.VALIDATE_CART_ICON_PROPERTY)
            if cart_icons and cart_icons[0].is_displayed():
                return "success", cart_icons[0]
            return False
        
        outcome, element = wait_until(self.driver, login_outcome)

        if outcome == "error":
            return element.text

        return "passed"
