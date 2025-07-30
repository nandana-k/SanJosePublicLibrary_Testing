from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_multiple(self, *locator):
        return self.driver.find_elements(*locator)

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def click(self, locator):
        self.find(*locator).click()

    def get_text(self, locator):
        return self.find(*locator).text

    def wait_until_visible(self, *locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(*locator))
