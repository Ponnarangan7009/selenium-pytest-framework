from selenium.webdriver.common.by import By
from util.selenium_helpers import child_texts, click_when_ready, visible_text

class CartPage:
    HEADING = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_heading(self):
        return visible_text(self.driver, self.HEADING)

    def get_product_names(self):
        return child_texts(self.driver, self.CART_ITEMS, self.PRODUCT_NAME)

    def click_checkout(self):
        click_when_ready(self.driver, self.CHECKOUT_BUTTON)
