import os
import pytest
import requests

from core.config_loader import Config
from core.driver_factory import get_webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope="session", autouse=True)
def skip_ui_tests_in_ci():
    """
    In CI (e.g. GitHub Actions), skip Selenium UI tests entirely.

    Reason:
    - Tests depend on an external demo app (https://www.saucedemo.com/)
    - In headless/CI environments the app may behave differently
      (bot protection, layout changes, overlays), causing flaky failures.

    Locally:
    - CI env var is usually not set, so tests run normally.
    """
    if os.getenv("CI") == "true":
        pytest.skip(
            "UI Selenium tests are skipped in CI. "
            "Run the test suite locally to execute browser tests."
        )


@pytest.fixture(scope="session")
def config():
    return Config()


@pytest.fixture(scope="session")
def app_available(config):
    """
    Verify that the application under test is reachable and looks like
    the expected SauceDemo login page.

    If not, skip the entire test session (when running locally).
    """
    url = config.base_url

    try:
        response = requests.get(url, timeout=10)
    except Exception as exc:
        pytest.skip(f"Base URL not reachable: {exc}")

    if response.status_code != 200:
        pytest.skip(
            f"Base URL returned unexpected status code: {response.status_code}"
        )

    # Basic sanity check – SauceDemo login page normally contains "Swag Labs"
    if "Swag Labs" not in response.text:
        pytest.skip(
            "Application content did not match expected SauceDemo login page."
        )


@pytest.fixture(scope="session")
def driver(config, app_available):
    """
    Provide a single WebDriver instance for the test session.

    Depends on app_available fixture, so if the app is not reachable
    or looks wrong (locally), tests are skipped gracefully.
    """
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
