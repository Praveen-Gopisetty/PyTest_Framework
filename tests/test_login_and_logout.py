import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import logging
import time
from utils.config_reader import ConfigReader

@pytest.mark.regression
def test_login_and_logout(browser):
    browser.get("https://www.saucedemo.com/")
    logging.info("This is a log message")
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    assert inventory_page.is_inventory_displayed()

    inventory_page.logout()
    assert "saucedemo" in browser.current_url

@pytest.mark.smoke
@pytest.mark.parametrize("username", [
    'standard_user',
    'problem_user',
    'visual_user',
])
def test_multiple_login(browser, username):

    password = ConfigReader.get_password(username)
    browser.get("https://www.saucedemo.com/")
    logging.info("This is a log message")

    login_page = LoginPage(browser)
    login_page.login(username, password)

    time.sleep(3)

    inventory_page = InventoryPage(browser)
    assert inventory_page.is_inventory_displayed(), \
        f"Inventory page not displayed for user: {username}"

    inventory_page.logout()
    assert "saucedemo" in browser.current_url


@pytest.mark.regression
def test_failure_case(browser):
    browser.get("https://www.saucedemo.com/")

    login_page = LoginPage(browser)
    login_page.login("standard_use", "hjvjjjh")

    inventory_page = InventoryPage(browser)
    assert inventory_page.is_inventory_displayed()

    inventory_page.logout()
    assert "saucedemo" in browser.current_url


