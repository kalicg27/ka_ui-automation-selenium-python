import pytest
from core.config_loader import Config
from core.driver_factory import get_webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope="session")
def config():
    return Config()


@pytest.fixture(scope="session")
def driver(config):
    driver = get_webdriver(config)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver, config):
    page = LoginPage(driver)
    page.open_login_page(config.base_url)
    return page


@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)
