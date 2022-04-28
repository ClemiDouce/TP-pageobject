from selenium import webdriver

def test__amazon():
    driver = webdriver.Chrome()
    driver.get("http://amazon.fr/")
    driver.maximize_window()
    driver.quit()