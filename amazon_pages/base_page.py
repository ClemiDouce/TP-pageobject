from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(driver, 10)

    def wait_and_click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def wait_and_read(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator)).text
