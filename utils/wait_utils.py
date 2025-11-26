from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def wait_for_element_visible(
    driver: WebDriver,
    locator: tuple[By, str],
    timeout: int = 15
):
    """
    Wait until the given locator is visible and return the WebElement.

    :param driver: Selenium WebDriver instance
    :param locator: Tuple of (By, locator_string)
    :param timeout: Max time in seconds to wait
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
