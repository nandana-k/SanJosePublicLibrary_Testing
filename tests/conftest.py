import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime

now = datetime.now()
timestamp_str = now.strftime("%Y%m%d_%H%M%S")
filename = f"test_failure_{timestamp_str}.png"

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        driver.save_screenshot(filename)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="https://www.sjpl.org")

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")

@pytest.fixture
def driver():
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()