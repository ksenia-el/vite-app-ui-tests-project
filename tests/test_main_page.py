#  file to collect all tests created for main page

from pages.main_page import MainPage
from pages.main_page import AuthMainPage
from pages.main_page import UnAuthMainPage
from config import Links
from tests.test_data import TestData
from pages.locators import MainPageLocators
import pytest
import time


# tests UI elements available for both authorized and non-authorized users

#  although browser-fixture (which creates a browser window) is run automatically for every function with test,
#  (and so there is no need to call it explicitly) - we still mention it in the parameters for functions with tests -
#  just to be able to refer to this browser window for executing some processes inside functions


class TestMainPage:

    #  tests whether filter by pet type works
    #  (verifies every pet type possible to use in filter according to Links.pet_types_in_filter)
    @pytest.mark.parametrize("pet_type", TestData.pet_types_in_filter)  # by that we parametrize the function by fixture
    # and so it will run tests with different values of pet type parameter in filter
    @pytest.mark.regress
    @pytest.mark.flaky
    def test_filter_by_type(self, browser, pet_type):
        main_page = MainPage(browser, Links.main_page_link)  # by that we create a page object and it will
        # automatically open the main page
        main_page.filter_by_type(pet_type)
        list_of_pet_types_shown = main_page.get_types_of_pets_shown()
        #  print(list_of_pet_types_shown)
        for type_shown in list_of_pet_types_shown:
            if type_shown != pet_type:
                raise AssertionError(f"Wrong filtering result (expected: by type '{pet_type}', found: '{type_shown}')")

    #  tests whether filter by pet name works
    #  (verifies every pet name mentioned in TestData.pet_names_in_filter)
    @pytest.mark.parametrize("pet_name", TestData.pet_names_in_filter)
    @pytest.mark.regress
    @pytest.mark.flaky
    def test_filter_by_name(self, browser, pet_name):
        main_page = MainPage(browser, Links.main_page_link)
        main_page.filter_by_pet_name(pet_name)
        list_of_names_shown = main_page.names_of_pets_shown()
        print(list_of_names_shown)
        for name_shown in list_of_names_shown:
            if name_shown != pet_name:
                raise AssertionError(f"Wrong filtering result (expected: by name '{pet_name}', found: '{name_shown}'")


#  tests UI-elements available for non-authorized users
#  (whether navigation elements such as Login link, Register link, Main Page link works)
class TestUnAuthMainPage:
    @pytest.mark.smoke
    def test_navigation_elements(self, browser):
        main_page = UnAuthMainPage(browser, Links.main_page_link)
        assert main_page.logo_button_exist(), "Wrong result, no Logo button found"
        main_page.go_to_login_page()  # and run function on it
        assert browser.current_url == Links.login_page, f"Wrong result, didn't navigate to Login page"
        main_page.open_page()
        main_page.go_to_register_page()
        assert browser.current_url == Links.register_page, f"Wrong result, didn't navigate to Register page"


#  tests whether navigation from the main page to the login page works
#  although browser fixture (to create a browser) is executed implicitly for every test we still mention it
#  just to be able to use browser from fixture in some other processes inside the test
#  and by mentioning login fixture in parameters we execute login process
#  tests UI-elements available for non-authorized users
class TestAuthMainPage:

    @pytest.mark.smoke
    def test_navigation_elements(self, browser, login):
        main_page = AuthMainPage(browser, Links.main_page_link)
        assert main_page.logo_button_exist(), "Wrong result, no Logo button found"
        main_page.go_to_profile_page()
        assert browser.current_url == Links.profile_page, f"Wrong result, didn't navigate to Profile page"
        main_page.open_page()
        main_page.log_out()
        assert main_page.login_button_exists(), f"Wrong result, the logout process failed (no 'Login' button found)"
