from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EventsPage(BasePage):

    events = (By.XPATH, "//div[@class='cp-events-search-item']")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.url = f"{base_url}/events"

    def load(self):
        self.visit(self.url)

    def title_contains(self, text):
        return text.lower() in self.driver.title.lower()

    def event_listings(self):
        return self.find_multiple(*self.events)
