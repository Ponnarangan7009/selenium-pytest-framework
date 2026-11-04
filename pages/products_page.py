from selenium.webdriver.common.by import By
from util.selenium_helpers import (
    child_texts,
    click_element_when_ready,
    click_when_ready,
    visible_elements,
    visible_text,
    wait_until,
)


class ProductsPage:
    PRODUCTS_HEADING = (By.CLASS_NAME, "title")
    PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test^='add-to-cart-']")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver

    def get_heading(self):
        return visible_text(self.driver, self.PRODUCTS_HEADING)

    def add_product_to_cart(self, product_name):
        cards = visible_elements(self.driver, self.PRODUCT_CARDS)

        for card in cards:
            name = card.find_element(*self.PRODUCT_NAME).text

            if name == product_name:
                button = card.find_element(*self.ADD_TO_CART_BUTTON)
                add_button_test_id = button.get_attribute("data-test")
                click_element_when_ready(self.driver, button)
                remove_button_test_id = add_button_test_id.replace(
                    "add-to-cart-", "remove-", 1
                )
                wait_until(
                    self.driver,
                    lambda browser: browser.find_elements(
                        By.CSS_SELECTOR,
                        f"button[data-test='{remove_button_test_id}']",
                    ),
                )
                return

        raise AssertionError(f"Product not found: {product_name}")

    def get_cart_count(self):
        return visible_text(self.driver, self.CART_BADGE)

    def open_cart(self):
        click_when_ready(self.driver, self.CART_LINK)

    def get_cart_product_names(self):
        return child_texts(self.driver, self.CART_ITEMS, self.PRODUCT_NAME)
