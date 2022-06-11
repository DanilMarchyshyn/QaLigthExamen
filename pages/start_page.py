from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from constants.login import LoginConstants
from pages.base_page import BasePage
from constants.header import HeaderConstants
from pages.footer_page import FooterPage
from pages.header_page import HeaderPage
from pages.register_page import RegisterPage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constant = HeaderConstants()
        self.constants = LoginConstants()
        self.header = HeaderPage(driver)
        self.footer = FooterPage(driver)
        self.register = RegisterPage(driver)

    def login(self, email="", password=""):
        """"Login provide value"""
        self.fill_field(attributes=By.NAME, locator=self.constants.EMAIL_FIELD_NAME, value=email)
        self.fill_field(attributes=By.XPATH, locator=self.constants.PASSWORD_FIELD_XPATH, value=password)
        self.click(attributes=By.XPATH, locator=self.constants.LOGIN_BUTTON_XPATH)

    def verify_invalid_error_message(self):
        """Verify error Invalid email ot password for login"""
        error_message_invalid = self.driver.find_element(By.XPATH, value=self.constants.ERROR_MESSAGE_INVALID_XPATH)
        assert error_message_invalid.text == self.constants.ERROR_MESSAGE_INVALID_TEXT

    def verify_required_error_message(self):
        """Verify error field is required for login"""
        error_message_email = self.driver.find_element(By.XPATH, value=self.constants.ERROR_MESSAGE_EMAIL_XPATH)
        error_message_password = self.driver.find_element(By.XPATH, value=self.constants.ERROR_MESSAGE_PASSWORD_XPATH)
        assert error_message_email.text == error_message_password.text == self.constants.ERROR_MESSAGE_REQUIRED_TEXT

    def click_acc_link(self):
        """Click on link 'Create an account'"""
        self.click(attributes=By.XPATH, locator=self.constants.CREATE_ACC_LINK_XPATH)
