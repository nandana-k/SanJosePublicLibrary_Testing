from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    dashboard_header = (By.XPATH, "//span[text()='You Belong']")
    navigation_links = (By.CSS_SELECTOR, "nav.main-menu a")
    footer_name = (By.TAG_NAME, "footer")
    search_bar = (By.XPATH, "//input[@testid='main_search_input']")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.url = base_url

    def load(self):
        self.visit(self.url)

    def title_contains(self, text):
        return text in self.driver.title

    def search_box(self):
        return self.find(*self.search_bar)

    def nav_links(self):
        return self.find_multiple(*self.navigation_links)

    def footer(self):
        return self.find(*self.footer_name)

    def is_dashboard_header_displayed(self):
        return self.find(*self.dashboard_header).is_displayed()
