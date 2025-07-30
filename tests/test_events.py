from pages.events_page import EventsPage
from tests.base_test import BaseTest

class TestContact(BaseTest):

    def test_events_page_loads(self, driver, base_url):
        events = EventsPage(driver, base_url)
        events.load()
        assert events.title_contains("Events")
        assert len(events.event_listings()) > 0
