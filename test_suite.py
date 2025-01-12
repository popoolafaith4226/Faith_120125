import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from ActionPage.actionStep import LoginPage

# Desired Capabilities for Appium
capabilities = {

    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "platformVersion": "15",
    "app": r"C:\\Users\\Quality Assurance\\Downloads\\Mobile_UI_Automation\\Mobile_UI_Automation\\App\\Android\\QAtestbuild22ndJan.apk",
    "appPackage": "com.wemabank.alat.office.alat_qa_test",
    "uiautomator2ServerInstallTimeout": 6000,
    # Optional capabilities to start the emulator in headless mode
    "noReset": True,  # Prevent resetting the app state before the session starts

}


appium_server_url = 'http://localhost:4723/wd/hub'


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.implicitly_wait(10)
    yield driver
    time.sleep(20)
    driver.quit()


def test_login_workflow(driver):
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.enter_username("test@user1.com")
    login_page.enter_password("Password1")
    login_page.submit_login()

