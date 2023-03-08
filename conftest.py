#  file to collect all fixtures

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import Links
from pages.locators import LoginPageLocators
from tests.test_data import TestData
import time


#  fixture to create a browser window
#  automatically & implicitly run for every test-function (done by "autouse" parameter)
@pytest.fixture(autouse=True)  # by autouse parameter the fixture is executed automatically and implicitly in the
# beginning of every test
def browser():
    browser = webdriver.Chrome(service=Service(executable_path='./chromedriver'))
    yield browser
    browser.quit()


#  fixture to login on the website - starts from login page and finishes on the profile page
@pytest.fixture()
def login(browser):
    browser.get(Links.login_page)
    login_field = browser.find_element(*LoginPageLocators.LOGIN_FIELD)
    login_credentials = TestData.valid_username_and_password_pairs[0]
    for login in login_credentials.keys():
        login_field.send_keys(login)
        password_field = browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(login_credentials[login])
        #  time.sleep(3)
    submit_button = browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    submit_button.submit()
