#  file that contains main page class

from pages.base_page import BasePage
from pages.locators import MainPageLocators
import time
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):  # by mentioning BaseClass in parameters we don't need to specify the constructor of this
    # spec class -  it's already here (invisible)

    #  filter cards by pet type
    def filter_by_type(self, pet_type):
        filter_dropdown = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE_DROPDOWN)
        filter_dropdown.click()
        time.sleep(1)
        all_types_of_pets = self.browser.find_elements(*MainPageLocators.ALL_PET_TYPES_IN_FILTER)
        for type_element in all_types_of_pets:
            if type_element.text == pet_type:
                type_element.click()
                time.sleep(1)
                return

    def get_types_of_pets_shown(self):
        pet_types_elements = self.browser.find_elements(*MainPageLocators.PET_TYPES_SHOWN_ON_PAGE)
        pet_types_list = []
        for pet_type_element in pet_types_elements:
            pet_types_list.append(pet_type_element.text)
        unique_types = set(pet_types_list)  # by that we choose only unique values for types
        return unique_types

    def filter_by_pet_name(self, pet_name):
        pet_name_input_field = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME_FIELD)
        pet_name_input_field.click()
        pet_name_input_field.send_keys(pet_name)
        pet_name_input_field.send_keys(Keys.ENTER)
        time.sleep(1)

    #  returns the list of strings - unique names of pets detected on the page
    def names_of_pets_shown(self):
        pet_names_elements = self.browser.find_elements(*MainPageLocators.PET_NAMES_SHOWN_ON_PAGE)
        pet_names_list = []
        for pet_name_element in pet_names_elements:
            pet_names_list.append(pet_name_element.text)
        unique_names = set(pet_names_list)
        return unique_names

    def login_button_exists(self):
        login_button_elements = self.browser.find_elements(*MainPageLocators.LOGIN_BUTTON)
        if len(login_button_elements) == 1:
            return True
        else:
            return False

    def logo_button_exist(self):
        logo_button_elements = self.browser.find_elements(*MainPageLocators.LOGO_BUTTON)
        return len(logo_button_elements) == 1


class UnAuthMainPage(MainPage):

    def go_to_login_page(self):  # by mentioning browser we actually call a fixture to open it
        login_button = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)  # by that we find login button (by
        # the locator imported from class of all locators for this page)
        login_button.click()

    def go_to_register_page(self):
        register_button = self.browser.find_element(*MainPageLocators.REGISTER_BUTTON)
        register_button.click()


class AuthMainPage(MainPage):

    def go_to_profile_page(self):
        profile_button = self.browser.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_button.click()

    #  function that clicks on the "Quit" button and logs out
    def log_out(self):
        quit_button = self.browser.find_element(*MainPageLocators.QUIT_BUTTON)
        quit_button.click()
