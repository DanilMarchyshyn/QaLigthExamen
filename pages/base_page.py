import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as MozilaDriver
from selenium.webdriver.support.wait import WebDriverWait
from constants.base import BaseConstants


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=10)

    def fill_field(self, attributes, locator, value):
        """Send data into the field"""
        field = self.driver.find_element(by=attributes, value=locator)
        field.click()
        field.clear()
        field.send_keys(value)

    def click(self, attributes, locator):
        """Find and click element"""
        self.driver.find_element(by=attributes, value=locator).click()


def create_driver(browser: str):
    """Create driver driver according to provided browser"""
    if browser == BaseConstants.CHROME:
        options = webdriver.ChromeOptions()
        driver = ChromeDriver(options=options)
    elif browser == BaseConstants.FIREFOX:
        options = webdriver.firefox.webdriver.Options()
        options.add_argument("--headless")
        driver = MozilaDriver(options=options)
    else:
        raise ValueError(f"Unknown browser name: '{browser}'")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(BaseConstants.BASE_URL)
    return driver


def random_symbol(prefix, maxlen):
    """Generate random symbol"""
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
