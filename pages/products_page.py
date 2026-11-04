from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
        self.wait = WebDriverWait(driver, 10)

    def get_heading(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.PRODUCTS_HEADING)
        )
        return heading.text

    def add_product_to_cart(self, product_name):
        cards = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT_CARDS)
        )

        for card in cards:
            name = card.find_element(*self.PRODUCT_NAME).text

            if name == product_name:
                button = card.find_element(*self.ADD_TO_CART_BUTTON)
                self.wait.until(lambda _: button.is_enabled())
                button.click()
                return

        raise AssertionError(f"Product not found: {product_name}")

    def get_cart_count(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return badge.text

    def open_cart(self):
        cart_link = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()

    def get_cart_product_names(self):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.CART_ITEMS)
        )
        return [
            item.find_element(*self.PRODUCT_NAME).text
            for item in items
        ]