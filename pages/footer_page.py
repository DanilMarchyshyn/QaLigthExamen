from selenium.webdriver.common.by import By

from constants.footer import FooterConstants
from pages.base_page import BasePage


class FooterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = FooterConstants()

    def verify_logout_link(self):
        """Verify 'Logout' link on footer"""
        element_logout = self.driver.find_element(By.XPATH, value=self.constants.LOGOUT_LINK_XPATH)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element_logout)
        assert element_logout.text == self.constants.LOGOUT_LINK_TEXT
