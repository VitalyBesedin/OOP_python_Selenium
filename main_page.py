from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def select_product(self, product_link): # choose and add the product to the cart

        select_product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, product_link)))
        select_product.click()
        print("Click Select Product")
