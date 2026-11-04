from selenium.webdriver.common.by import By
from util.selenium_helpers import (
    child_texts,
    click_when_ready,
    visible_element,
    visible_text,
)


class CheckoutPage:
    HEADING = (By.CLASS_NAME, "title")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def get_heading(self, expected_text):
        return visible_text(self.driver, self.HEADING, expected_text)

    def enter_customer_information(self, first_name, last_name, postal_code):
        visible_element(self.driver, self.FIRST_NAME).send_keys(first_name)

        visible_element(self.driver, self.LAST_NAME).send_keys(last_name)
        visible_element(self.driver, self.POSTAL_CODE).send_keys(postal_code)

    def continue_to_overview(self):
        click_when_ready(self.driver, self.CONTINUE_BUTTON)


class CheckoutOverviewPage:
    HEADING = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def get_heading(self, expected_text):
        return visible_text(self.driver, self.HEADING, expected_text)

    def get_product_names(self):
        return child_texts(self.driver, self.CART_ITEMS, self.PRODUCT_NAME)

    def finish_checkout(self):
        click_when_ready(self.driver, self.FINISH_BUTTON)


class CheckoutCompletePage:
    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_message(self):
        return visible_text(self.driver, self.CONFIRMATION_MESSAGE)

    def get_back_home_button_text(self):
        return visible_text(self.driver, self.BACK_HOME_BUTTON)
