from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def is_loaded(self) -> bool:
        return self.is_visible(self.INVENTORY_CONTAINER)

    def add_item_to_cart(self, item_name: str):
        # item_name example: "Sauce Labs Backpack"
        locator = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        self.click(locator)

    def go_to_cart(self):
        self.click(self.CART_BUTTON)

    def get_cart_count(self) -> int:
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0
