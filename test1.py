import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Test_1():
    def test_select_product(self):
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        # g = Service()
        # driver = webdriver.Chrome(options=options, service=g)  # this is and above macOS
        # driver = webdriver.Chrome()  # Windows
        # driver = webdriver.Firefox()
        driver = webdriver.Safari()
        # driver = webdriver.Edge()
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(5)

test = Test_1()
test.test_select_product()

