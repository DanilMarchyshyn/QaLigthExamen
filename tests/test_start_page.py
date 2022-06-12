import pytest

from pages.base_page import create_driver, random_symbol
from constants.base import BaseConstants
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

        start_page.header.login_header()
        start_page.login()
        start_page.verify_required_error_message()

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
        start_page.login(email=random_symbol("Test", 3), password="P@ssw0rd")
        start_page.verify_invalid_error_message()

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
        start_page.login(email="testqaligth@yopmail.com", password="Incorrect")
        start_page.verify_invalid_error_message()

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
        start_page.login(email="testqaligth@yopmail.com", password="P@ssw0rd")
        start_page.footer.verify_logout_link()

    def test_create_account_without_agree_terms(self, start_page):
        """
        - create driver
        - open main page
        - click button Get Started
        - fill field 'Full Name' with correct value
        - fill field 'Email' with correct value
        - fill field 'Password' with correct value
        - fill field 'Phone' with correct value
        - click button 'Create my account'
        - verify error message agree terms
        """

        start_page.header.click_get_started_button()
        start_page.register.register_fill_field(fullname="Test", email=random_symbol("Test", 7) + "@yopmail.com",
                                                password="P@ssw0rd", phone="0501112233")
        start_page.register.click_create_acc_button()
        start_page.register.verify_agree_terms_error_message()

    def test_empty_fullname_email_register(self, start_page):
        """
        - create driver
        - open main page
        - click button Get Started
        - fill field 'Full Name' with empty value
        - fill field 'Email' with empty value
        - fill field 'Password' with correct value
        - fill field 'Phone' with correct value
        - click checkbox 'I agree terms...'
        - click button 'Create my account'
        - verify error This field is required!
        """

        start_page.header.click_get_started_button()
        start_page.register.register_fill_field(fullname="", email="",
                                                password="P@ssw0rd", phone="0501112233")
        start_page.register.click_agree_checkbox()
        start_page.register.click_create_acc_button()
        start_page.register.verify_required_error_message()
