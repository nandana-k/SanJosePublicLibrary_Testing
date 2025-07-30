import pytest

from pages.search_page import SearchPage
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from utilities.test_data import TestData
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("driver", "log_on_failure")
class TestLogin(BaseTest):

    place_hold_button = (By.XPATH, "//button[@data-key='bib-place-a-hold'][1]")
    hold_message = (By.XPATH, "//span[@id='message_item_hold_placed_no_position']")
    cancel_hold_button = (By.XPATH, "//button[@class='cp-btn btn btn-secondary cp-cancel-hold-button btn-block']")
    confirm_cancel_button = (By.XPATH, "//button[@data-test-id='confirm-cancel-hold']")
    cancel_message = (By.XPATH, "//div[@class='alert-content']")
    account_button = (By.XPATH, "//div[@class='biblio_bar_my_account']")
    log_out_button = (By.XPATH, "//a[@class='btn btn-transactional btn-block log_out_btn']")

    @pytest.mark.parametrize("inv_username, inv_password", [("1234", "0000"), ("9012314214", "1111")])
    def test_login_error_message(self, driver, base_url, inv_username, inv_password):
        login = LoginPage(driver, base_url)
        login.load()
        login.set_username(inv_username)
        login.set_password(inv_password)
        login.click_login_button()
        actual_message = login.get_error_message()
        assert "username or PIN is incorrect" in actual_message

    def test_place_hold(self, driver, base_url):
        login = LoginPage(driver, base_url)
        login.load()
        login.log_into_application(TestData.valid_username, TestData.valid_password)
        search = SearchPage(driver, base_url)
        search.search("heaven")
        place_hold_button = search.find(*self.place_hold_button)
        place_hold_button.click()
        hold_message = search.find(*self.hold_message)
        assert "Hold requested on" in hold_message.text
        actions = ActionChains(driver)
        account_button = search.find(*self.account_button)
        actions.move_to_element(account_button).click().perform()
        log_out_button = search.find(*self.log_out_button)
        actions.move_to_element(log_out_button).click().perform()

    def test_cancel_hold(self, driver, base_url):
        login = LoginPage(driver, base_url)
        login.load()
        login.log_into_application(TestData.valid_username, TestData.valid_password)
        search = SearchPage(driver, base_url)
        search.search("heaven")
        cancel_hold_button = search.find(*self.cancel_hold_button)
        cancel_hold_button.click()
        confirm_cancel_button = search.find(*self.confirm_cancel_button)
        confirm_cancel_button.click()
        cancel_message = search.find(*self.cancel_message)
        assert "Successfully canceled" in cancel_message.text
        actions = ActionChains(driver)
        account_button = search.find(*self.account_button)
        actions.move_to_element(account_button).click().perform()
        log_out_button = search.find(*self.log_out_button)
        actions.move_to_element(log_out_button).click().perform()




