from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT  = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON  = (By.ID, "continue")
    FINISH_BUTTON    = (By.ID, "finish")
    SUCCESS_MESSAGE  = (By.CSS_SELECTOR, "h2.complete-header")

    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self) -> str:
        return self.get_text(self.SUCCESS_MESSAGE)
