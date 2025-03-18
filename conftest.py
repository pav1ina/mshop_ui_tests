from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.create_account_page import CreateAccount
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sales_page import SalesPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


@pytest.fixture()
def create_new_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sales_page(driver):
    return SalesPage(driver)
