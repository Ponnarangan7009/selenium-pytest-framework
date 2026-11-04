from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    HEADING = (By.CLASS_NAME, "title")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_heading(self, expected_text):
        self.wait.until(
            lambda driver: (
                (heading := driver.find_element(*self.HEADING)).is_displayed()
                and heading.text.strip() == expected_text
            )
        )
        return self.driver.find_element(*self.HEADING).text.strip()

    def enter_customer_information(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)

        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def continue_to_overview(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        button.click()


class CheckoutOverviewPage:
    HEADING = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_heading(self, expected_text):
        self.wait.until(
            lambda driver: (
                (heading := driver.find_element(*self.HEADING)).is_displayed()
                and heading.text.strip() == expected_text
            )
        )
        return self.driver.find_element(*self.HEADING).text.strip()

    def get_product_names(self):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.CART_ITEMS)
        )
        return [
            item.find_element(*self.PRODUCT_NAME).text
            for item in items
        ]
