#  file to collect all tests created for main page
import config
from pages.login_page import LoginPage
from config import Links
from tests.test_data import TestData
from pages.locators import LoginPageLocators
import pytest
import time


class TestLoginPage:

    # tests login functionality with valid credentials
    # (credentials are collected in TestData.valid_username_and_password_pairs)
    @pytest.mark.parametrize("credentials", TestData.valid_username_and_password_pairs)
    @pytest.mark.smoke
    @pytest.mark.regress
    def test_login_with_valid(self, browser, credentials):
        login_page = LoginPage(browser, Links.login_page)
        login_page.login(credentials)
        time.sleep(2)
        assert browser.current_url == Links.profile_page, f"Wrong result, expected to be on profile page"

    # tests login functionality with invalid credentials
    # (credentials are collected in TestData.invalid_username_and_password_pairs)
    @pytest.mark.parametrize("credentials", TestData.invalid_username_and_password_pairs)
    @pytest.mark.smoke
    @pytest.mark.regress
    def test_login_with_invalid(self, browser, credentials):
        login_page = LoginPage(browser, Links.login_page)
        login_page.login(credentials)
        time.sleep(2)
        assert browser.current_url == Links.login_page, f"Wrong result, expected to stay on login page"
        assert login_page.error_message_shown(), f"Wrong result, no error message shown"

    #  tests navigation elements (Logo Button, Login button and Register button) on the page
    @pytest.mark.smoke
    def test_navigation_elements(self, browser):
        login_page = LoginPage(browser, Links.login_page)
        assert login_page.login_button_exist(), f"Wrong result, no 'Login' navigation button found"
        login_page.navigate_to_registration_page()
        assert browser.current_url == Links.register_page, f"Wrong result, expected to be redirected to the Register page"
        login_page.open_page()
        login_page.navigate_to_main_page()
        assert browser.current_url == Links.main_page_link, f"Wrong result, expected to be redirected to the Main page"
