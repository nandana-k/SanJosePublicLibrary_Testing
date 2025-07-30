from pages.contact_page import ContactPage
from tests.base_test import BaseTest

class TestContact(BaseTest):

    def test_contact_page_loads(self, driver, base_url):
        contact = ContactPage(driver, base_url)
        contact.load()
        assert contact.title_contains("Contact")
        assert contact.form() is not None