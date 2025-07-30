from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):

    form_name = (By.TAG_NAME, "form")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.url = f"{base_url}/contact"

    def load(self):
        self.visit(self.url)

    def form(self):
        return self.find(*self.form_name)

    def title_contains(self, keyword):
        return keyword.lower() in self.driver.title.lower()
