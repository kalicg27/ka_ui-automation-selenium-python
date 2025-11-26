from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.wait_utils import wait_for_element_visible


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def click(self, locator: tuple[By, str]):
        element = wait_for_element_visible(self.driver, locator)
        element.click()

    def type(self, locator: tuple[By, str], text: str, clear: bool = True):
        element = wait_for_element_visible(self.driver, locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple[By, str]) -> str:
        element = wait_for_element_visible(self.driver, locator)
        return element.text

    def is_visible(self, locator: tuple[By, str]) -> bool:
        try:
            wait_for_element_visible(self.driver, locator)
            return True
        except TimeoutException:
            return False
