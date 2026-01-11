import pytest
from selenium import webdriver
import allure

@pytest.fixture(scope="session")
def browser():

    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    # 🔴 Disable Google services that trigger breach popup
    options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordCheck")

    # 🔴 Run Chrome without user profile / sync
    options.add_argument("--disable-sync")
    options.add_argument("--disable-infobars")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            png = driver.get_screenshot_as_png()
            allure.attach(
                png,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )