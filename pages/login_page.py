import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    username_field = (By.XPATH, "//input[@testid='field_username']")
    pin_field = (By.XPATH, "//input[@testid='field_userpin']")
    login_button = (By.XPATH, "//input[@value='Log In']")
    error_message = (By.XPATH, "//p[@data-test-id='top-message']")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.url = "https://sjpl.bibliocommons.com/user/login"

    def load(self):
        self.visit(self.url)

    def set_username(self, username):
        self.set(self.username_field, username)

    def set_password(self, password):
        self.set(self.pin_field, password)

    def click_login_button(self):
        self.click(self.login_button)
        time.sleep(2)
        #return DashboardPage(self.driver)

    def log_into_application(self, username, password):
        self.set_username(username)
        self.set_password(password)
        return self.click_login_button()

    def get_error_message(self):
        return self.get_text(self.error_message)
