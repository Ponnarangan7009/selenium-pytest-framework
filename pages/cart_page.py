from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    HEADING = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_heading(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.HEADING)
        )
        return heading.text

    def get_product_names(self):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.CART_ITEMS)
        )
        return [
            item.find_element(*self.PRODUCT_NAME).text
            for item in items
        ]

    def click_checkout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        button.click()