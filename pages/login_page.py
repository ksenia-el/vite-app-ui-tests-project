from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from config import Links
from tests.test_data import TestData


class LoginPage(BasePage):

    def login(self, login_credentials):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        for login in login_credentials.keys():
            login_field.send_keys(login)
            password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
            password_field.send_keys(login_credentials[login])
            #  time.sleep(3)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.submit()

    # navigates from the login page to the main page through the logo-button
    def navigate_to_main_page(self):
        logo_button = self.browser.find_element(*LoginPageLocators.LOGO_BUTTON)
        logo_button.click()

    def navigate_to_registration_page(self):
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def login_button_exist(self):
        login_button_elements = self.browser.find_elements(*LoginPageLocators.LOGIN_BUTTON)
        return len(login_button_elements) == 1

    # in case of unsuccessful login
    def error_message_shown(self):
        error_message_elements = self.browser.find_elements(*LoginPageLocators.ERROR_MESSAGE)
        return len(error_message_elements) == 1






