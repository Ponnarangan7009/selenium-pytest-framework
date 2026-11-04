from pages.login_page import LoginWebPage
import pytest

class TestLoginPage:

    @pytest.mark.parametrize(('username', 'password', 'message'), 
                             [
                                 ('standard_user', 'secret_sauce', 'passed'),
                                 ('error_user', 'secret_sauce', 'passed')
                                 ])
    @pytest.mark.smoke
    def test_valid_user(self, driver, username, password, message):
        page = LoginWebPage(driver)
        page.open_url()
        page.enter_login_username(username)
        page.enter_login_password(password)
        page.submit_form()
        result =  page.validate_user()

        assert result == message

    @pytest.mark.parametrize(('username', 'password', 'message'), 
                                 [
                                     ('someone', 'secret_sauce','sadface' ),
                                     ('locked_out_user', 'secret_sauce', 'sadface')
                                     ])
    @pytest.mark.regression
    def test_invalid_user(self, driver, username, password, message):
        page = LoginWebPage(driver)
        page.open_url()
        page.enter_login_username(username)
        page.enter_login_password(password)
        page.submit_form()
        result =  page.validate_user()

        assert message in result 

    