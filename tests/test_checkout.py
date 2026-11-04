import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage, CheckoutOverviewPage
from pages.login_page import LoginWebPage
from pages.products_page import ProductsPage


class TestCheckout:

    @pytest.mark.regression
    def test_checkout_to_overview(self, driver):
        login_page = LoginWebPage(driver)
        login_page.open_url()
        login_page.enter_login_username("standard_user")
        login_page.enter_login_password("secret_sauce")
        login_page.submit_form()

        assert login_page.validate_user() == "passed"

        products_page = ProductsPage(driver)
        assert products_page.get_heading() == "Products"
        products_page.add_product_to_cart("Sauce Labs Backpack")
        products_page.open_cart()

        cart_page = CartPage(driver)
        assert cart_page.get_heading() == "Your Cart"
        assert cart_page.get_product_names() == ["Sauce Labs Backpack"]
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        assert (
            checkout_page.get_heading("Checkout: Your Information")
            == "Checkout: Your Information"
        )
        checkout_page.enter_customer_information(
            "Test",
            "Learner",
            "12345",
        )
        checkout_page.continue_to_overview()

        overview_page = CheckoutOverviewPage(driver)
        assert (
            overview_page.get_heading("Checkout: Overview")
            == "Checkout: Overview"
        )
        assert overview_page.get_product_names() == ["Sauce Labs Backpack"]
