from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LocatorsPage.locators import LoginPageLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD)
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD)
        )
        password_field.send_keys(password)

    def submit_login(self):
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.SUBMIT_BUTTON)
        )
        submit_button.click()

