from selenium.webdriver.common.by import By

from constants.register import RegisterConstants
from pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = RegisterConstants()

    def register_fill_field(self, fullname="", email="", password=""):
        """Register provide value"""
        self.fill_field(attributes=By.NAME, locator=self.constants.FULLNAME_FIELD_NAME, value=fullname)
        self.fill_field(attributes=By.NAME, locator=self.constants.EMAIL_FIELD_NAME, value=email)
        self.fill_field(attributes=By.XPATH, locator=self.constants.PASSWORD_FIELD_XPATH, value=password)

    def click_agree_checkbox(self):
        """Click on 'I agree to the Terms and Conditions' checkbox"""
        self.click(attributes=By.XPATH, locator=self.constants.TERMS_CHECKBOX_XPATH)

    def click_create_acc_button(self):
        """Click on 'Create my account' button"""
        self.click(attributes=By.XPATH, locator=self.constants.CREATE_ACC_BUTTON_XPATH)

    def verify_agree_terms_error_message(self):
        """Verify error Invalid email ot password for login"""
        error_message_invalid = self.driver.find_element(By.XPATH, value=self.constants.ERROR_MESSAGE_AGREE_TERMS_XPATH)
        assert error_message_invalid.text == self.constants.ERROR_MESSAGE_AGREE_TERMS_TEXT
