from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.PARTIAL_LINK_TEXT, "Login")
    REGISTER_BUTTON = (By.PARTIAL_LINK_TEXT, "Register")
    LOGO_BUTTON = (By.CLASS_NAME, "p-menubar-start")
    FILTER_BY_TYPE_DROPDOWN = (By.ID, "typesSelector")
    ALL_PET_TYPES_IN_FILTER = (By.CSS_SELECTOR, 'ul.p-dropdown-items li')  # to get a list of all pet types available
    # in the filter
    PET_TYPES_SHOWN_ON_PAGE = (By.CLASS_NAME, "product-category")  # to collect pet types shown on the page
    FILTER_BY_NAME_FIELD = (By.ID, "petName")
    PET_NAMES_SHOWN_ON_PAGE = (By.CLASS_NAME, "product-name")  # to collect pet names shown on the page
    PROFILE_BUTTON = (By.PARTIAL_LINK_TEXT, "Profile")
    QUIT_BUTTON = (By.PARTIAL_LINK_TEXT, "Quit")


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "login")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "div#password > input")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGIN_BUTTON = (By.PARTIAL_LINK_TEXT, "Login")
    REGISTER_BUTTON = (By.PARTIAL_LINK_TEXT, "Register")
    LOGO_BUTTON = (By.CLASS_NAME, "p-menubar-start")
    ERROR_MESSAGE = (By.CLASS_NAME, "p-message-error")

# class ProfilePageLocators:
#     ADD_BUTTON = (By.CLASS_NAME, "p-button p-component p-button-icon-only p-button-rounded p-button-primary p-button-outlined")

