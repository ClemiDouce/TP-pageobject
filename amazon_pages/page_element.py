from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageElement:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # Utils
    def wait_and_click(self, by_locator):
        """Wait for an element to be clickable and click on it"""
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def wait_and_read(self, by_locator):
        """Wait for an element to appear and return his text"""
        return self.wait.until(EC.presence_of_element_located(by_locator)).text

    def enter_text(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def enter_text_and_valid(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text, Keys.ENTER)