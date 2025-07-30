from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):

    site_field = (By.XPATH, "//button[@title='Catalog']")
    catalog_filter_field = (By.XPATH, "//button[@title='Keyword']")
    site_filter_field = (By.XPATH, "//button[@title='All Content']")
    search_bar = (By.XPATH, "//input[@testid='main_search_input']")
    search_button = (By.XPATH, "//div[@id='header_search']//span[@class='input-group-btn']")
    website_button = (By.XPATH, "//div[@id='header_search']//span[text()='Website']")
    title_button = (By.XPATH, "//div[@id='header_search']//span[text()='Title']")
    author_button = (By.XPATH, "//div[@id='header_search']//span[text()='Author']")
    faq_button = (By.XPATH, "//div[@id='header_search']//li[@data-original-index='1']//span[text()='FAQs']")
    book_title = (By.XPATH, "//h2[@class='cp-title']")
    author_name = (By.XPATH, "//span[@class='cp-author-link']")
    languages_button = (By.XPATH, "//section[@class='cp-language-field']")
    english_filter = (By.XPATH, "//section[@class='cp-language-field']//label[@for='field-eng']")
    search_results = (By.CSS_SELECTOR, ".search-results .views-row")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.url = base_url

    def load(self):
        self.visit(self.url)

    def search(self, search_term):
        self.set(self.search_bar, search_term)
        self.click(self.search_button)

    def set_site_website(self):
        self.click(self.site_field)
        self.click(self.website_button)

    def set_filter_title(self):
        self.click(self.catalog_filter_field)
        self.click(self.title_button)

    def set_filter_author(self):
        self.click(self.catalog_filter_field)
        self.click(self.author_button)

    def set_filter_faq(self):
        self.click(self.site_filter_field)
        self.click(self.faq_button)

    def get_book_title(self):
        return self.find(self.book_title).text.lower()

    def get_author_name(self):
        return self.find(*self.author_name).text

    def get_book_titles(self):
        elements = self.find_multiple(*self.book_title)
        return [element.text.lower() for element in elements]

    def get_author_names(self):
        elements = self.find_multiple(*self.author_name)
        return [element.text.lower() for element in elements]

    def results(self):
        return self.find_multiple(*self.search_results)

    def title_contains(self, keyword):
        return keyword.lower() in self.driver.title.lower()