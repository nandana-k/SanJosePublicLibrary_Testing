import pytest
import time

from tests.base_test import BaseTest
from pages.search_page import SearchPage
from selenium.webdriver.common.by import By

class TestSearch(BaseTest):

    languages_button = (By.XPATH, "//section[@class='cp-language-field']")
    english_filter = (By.XPATH, "//section[@class='cp-language-field']//label[@for='field-eng']")
    faq_posts = (By.XPATH, "//h2[@class='entry-title c-post-excerpt__heading']")

    @pytest.mark.parametrize("catalog_keyword_search", ["artificial intelligence", "animal", "soccer"])
    def test_catalog_keyword_search(self, driver, base_url, catalog_keyword_search):
        search_page = SearchPage(driver, base_url)
        search_page.load()
        search_page.search(catalog_keyword_search)
        actual_book_titles = search_page.get_book_titles()
        for title in actual_book_titles:
            assert catalog_keyword_search in title.lower()

    @pytest.mark.parametrize("catalog_title_search", ["the catcher in the rye", "the kite runner"])
    def test_catalog_title_search(self, driver, base_url, catalog_title_search):
        search_page = SearchPage(driver, base_url)
        search_page.load()
        search_page.set_filter_title()
        search_page.search(catalog_title_search)
        languages_button = search_page.wait_until_visible(self.languages_button)
        languages_button.click()
        english_filter = search_page.find(*self.english_filter)
        english_filter.click()
        time.sleep(2)
        actual_book_titles = search_page.get_book_titles()
        for title in actual_book_titles:
            assert catalog_title_search in title.lower()

    @pytest.mark.parametrize("catalog_author_search", ["Austen, Jane", "Kafka, Franz", "Didion, Joan"])
    def test_catalog_author_search(self, driver, base_url, catalog_author_search):
        search_page = SearchPage(driver, base_url)
        search_page.load()
        search_page.set_filter_author()
        search_page.search(catalog_author_search)
        actual_author_name = search_page.get_author_name()
        assert catalog_author_search in actual_author_name

    def test_catalog_authors_search(self, driver, base_url):
        search_page = SearchPage(driver, base_url)
        search_page.load()
        search_page.set_filter_author()
        file_object = open('authors.txt', 'r')
        for line in file_object:
            author_search = line.strip().replace('"', '')
            search_page.search(author_search)
            time.sleep(2)
            actual_author_names = search_page.get_author_names()
            for author in actual_author_names:
                assert author_search.lower() in author

    @pytest.mark.parametrize("faq_search", ["fines", "library card"])
    def test_website_faq_search(self, driver, base_url, faq_search):
         search_page = SearchPage(driver, base_url)
         search_page.load()
         search_page.set_site_website()
         search_page.set_filter_faq()
         search_page.search(faq_search)
         faq_posts = search_page.find_multiple(*self.faq_posts)
         for post in faq_posts:
             assert faq_search in post.text.lower()
