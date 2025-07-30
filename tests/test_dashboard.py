import pytest

import requests
from pages.dashboard_page import DashboardPage
from tests.base_test import BaseTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestDashboard(BaseTest):

    link_names = (By.TAG_NAME, "a")
    mobile_header = (By.XPATH, "//div[@class ='cp_header_biblio_bar']")
    lang_button = (By.XPATH, "//select[@class ='gt_selector notranslate']")
    lang_options = (By.XPATH, "//select[@class='gt_selector notranslate']//option")

    def test_dashboard_header_is_displayed(self, driver, base_url):
        dashboard = DashboardPage(driver, base_url)
        dashboard.load()
        assert dashboard.is_dashboard_header_displayed(), f"\n Dashboard Header Is Not Displayed \n"

    def test_dashboard_page_loads(self, driver, base_url):
        dashboard = DashboardPage(driver, base_url)
        dashboard.load()
        assert dashboard.title_contains("San Jose Public Library")

    def test_search_functionality(self, driver, base_url):
        dashboard = DashboardPage(driver, base_url)
        dashboard.load()
        search_bar = dashboard.search_box()
        search_bar.send_keys("library")
        search_bar.send_keys(Keys.RETURN)
        assert "search" in driver.current_url

    def test_footer_visible(self, driver, base_url):
        dashboard = DashboardPage(driver, base_url)
        dashboard.load()
        footer = dashboard.footer()
        assert footer.is_displayed()

    def test_nav_links_work(self, driver, base_url):
        dashboard = DashboardPage(driver, base_url)
        dashboard.load()
        for link in dashboard.nav_links():
            href = link.get_attribute("href")
            assert href.startswith("https://")

    def test_no_broken_links_on_homepage(self, driver, base_url):
        dashboard = DashboardPage(driver, base_url)
        dashboard.load()
        links = dashboard.find_multiple(*self.link_names)
        hrefs = [link.get_attribute("href") for link in links if
                 link.get_attribute("href") and link.get_attribute("href").startswith("http")]
        for href in hrefs:
            response = requests.head(href, allow_redirects=True)
            assert response.status_code < 400, f"Broken link: {href} - Status: {response.status_code}"

    def test_mobile_view(self, driver, base_url):
        driver.set_window_size(375, 812)
        dashboard = DashboardPage(driver, base_url)
        dashboard.load()
        mobile_header = dashboard.find(*self.mobile_header)
        assert mobile_header.is_displayed()

    def test_language_toggle(self, driver, base_url):
        dashboard = DashboardPage(driver, base_url)
        dashboard.load()
        lang_button = dashboard.find(*self.lang_button)
        lang_button.click()
        options = dashboard.find_multiple(*self.lang_options)
        assert len(options) > 1