#  basic class for every page in the project
#  everything from here will be inherited by child classes of diff pages

class BasePage:
    #  constructor of the base page
    def __init__(self, browser, url, timeout=10):  # that is a class constructor
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # by that browser will implicitly spend 10 seconds to find every
        # web-element
        self.open_page()

    #  method of base page that will be inherited by every child class (=any page of the website)
    def open_page(self):
        self.browser.get(self.url)  # by that we open the url by the browser that were both passed as parameters
        # in class constructor









