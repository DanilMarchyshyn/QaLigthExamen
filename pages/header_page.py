from selenium.webdriver.common.by import By

from constants.header import HeaderConstants
from pages.base_page import BasePage


class HeaderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConstants()

    def login_header(self):
        """"Found and click Login on header"""
        self.click(attributes=By.CSS_SELECTOR, locator=self.constants.LOGIN_LINK_SELECTOR)

    def click_get_started_button(self):
        """Click on 'Get started' button """
        self.click(attributes=By.XPATH, locator=self.constants.GET_STARTED_BUTTON_XPATH)
