import time

import pytest

from pages.footer_page import FooterPage
from pages.base_page import create_driver, random_symbol
from constants.base import BaseConstants
from pages.login_page import LoginPage
from pages.start_page import StartPage


@pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestStartPage:
    @pytest.fixture(scope="function")
    def start_page(self, browser):
        driver = create_driver(browser)
        yield StartPage(driver)
        driver.close()

    def test_empty_fields_login(self, start_page):
        """
        - create driver
        - open main page
        - click link 'Log In'
        - clear field 'Email'
        - clear field 'Password'
        - click button 'Log In'
        - verify required error message
        """

        # start_page.login_header()
        start_page.header.login_header()
        time.sleep(2)
        start_page.login()
        time.sleep(5)
        start_page.verify_required_error_message()
        time.sleep(2)

    def test_invalid_email_login(self, start_page):
        """
        - create driver
        - open main page
        - click link 'Log In'
        - clear field 'Email'
        - fill field 'Email' with incorrect value
        - clear field 'Password'
        - fill field 'Password' with correct value
        - click button 'Log In'
        - verify invalid error message
        """

        start_page.header.login_header()
        time.sleep(2)
        start_page.login(email=random_symbol("Test", 3), password="P@ssw0rd")
        time.sleep(5)
        start_page.verify_invalid_error_message()
        time.sleep(2)

    # email_field = driver.find_element(By.NAME, 'email')
    # email = random_symbol("Test", 3)
    # password_field.send_keys("P@ssw0rd")

    def test_invalid_password_login(self, start_page):
        """
        - create driver
        - open main page
        - click link 'Log In'
        - clear field 'Email'
        - fill field 'Email' with correct value
        - clear field 'Password'
        - fill field 'Password' with incorrect value
        - click button 'Log In'
        - verify error message
        """

        start_page.header.login_header()
        time.sleep(2)
        start_page.login(email="testqaligth@yopmail.com", password="Incorrect")
        time.sleep(5)
        start_page.verify_invalid_error_message()
        time.sleep(2)

    def test_existing_user_login(self, start_page):
        """
        - create driver
        - open main page
        - click link Log In
        - clear field Email
        - fill field Email with correct value
        - clear field Password
        - fill field Password with correct value
        - click button Log In
        - verify on 'Logout' link
        """

        start_page.header.login_header()
        time.sleep(2)
        start_page.login(email="testqaligth@yopmail.com", password="P@ssw0rd")
        time.sleep(2)
        start_page.footer.verify_logout_link()
        time.sleep(2)

    # def test_create_valid_account(self, start_page):
    #     """
    #     - create driver
    #     - open main page
    #     - click link Log In
    #     - click link Create an account
    #     - fill field 'Full Name' with corect value
    #     - fill field 'Email' with corect value
    #     - fill field 'Password' with corect value
    #     - click checkbox 'I agree to the Terms and Conditions'
    #     - click button 'Create my account'
    #     - verify on 'Logout' link
    #     """
    #
    #     start_page.header.login_header()
    #     time.sleep(2)
    #     start_page.click_acc_link()
    #     time.sleep(2)
    #     start_page.register.register_fill_field(fullname="Test", email=random_symbol("Test", 7) + "@yopmail.com", password="P@ssw0rd")
    #     time.sleep(2)
    #     start_page.register.click_agree_checkbox()
    #     time.sleep(2)
    #     start_page.register.click_create_acc_button()
    #     time.sleep(20)
    #     start_page.footer.verify_logout_link()
    #     time.sleep(20)

    def test_create_account_without_agree_terms(self, start_page):
        """
        - create driver
        - open main page
        - click link Log In
        - click link Create an account
        - fill field 'Full Name' with corect value
        - fill field 'Email' with corect value
        - fill field 'Password' with corect value
        - click checkbox 'I agree to the Terms and Conditions'
        - click button 'Create my account'
        - verify on 'Login' button
        """

        start_page.header.login_header()
        time.sleep(2)
        start_page.click_acc_link()
        time.sleep(2)
        start_page.register.register_fill_field(fullname="Test", email=random_symbol("Test", 7) + "@yopmail.com",
                                                password="P@ssw0rd")
        time.sleep(2)
        start_page.register.click_create_acc_button()
        time.sleep(2)
        start_page.register.verify_agree_terms_error_message()
        time.sleep(2)
