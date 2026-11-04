import pytest

from pages.login_page import LoginWebPage
from pages.products_page import ProductsPage


class TestProductsAndCart:

    @pytest.mark.parametrize(
        "product_name",
        [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
        ],
    )
    @pytest.mark.regression
    def test_add_product_to_cart(self, driver, product_name):
        login_page = LoginWebPage(driver)
        login_page.open_url()
        login_page.enter_login_username("standard_user")
        login_page.enter_login_password("secret_sauce")
        login_page.submit_form()

        assert login_page.validate_user() == "passed"

        products_page = ProductsPage(driver)
        assert products_page.get_heading() == "Products"

        products_page.add_product_to_cart(product_name)

        assert products_page.get_cart_count() == "1"

        products_page.open_cart()

        assert products_page.get_cart_product_names() == [product_name]