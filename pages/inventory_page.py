from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")
    alert_popup = ()

    def is_inventory_displayed(self):
        return self.driver.find_element(*self.INVENTORY_CONTAINER).is_displayed()

    def logout(self):
        self.click(self.MENU_BTN)
        self.click(self.LOGOUT_BTN)

