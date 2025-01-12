from appium.webdriver.common.appiumby import AppiumBy


class LoginPageLocators:
    LOGIN_BUTTON = (AppiumBy.ID, 'com.wemabank.alat.office.alat_qa_test:id/loginBtn')
    EMAIL_FIELD = (AppiumBy.ID, 'com.wemabank.alat.office.alat_qa_test:id/email_input')
    PASSWORD_FIELD = (AppiumBy.ID, 'com.wemabank.alat.office.alat_qa_test:id/password_input')
    SUBMIT_BUTTON = (AppiumBy.ID, 'com.wemabank.alat.office.alat_qa_test:id/loginBtn')


