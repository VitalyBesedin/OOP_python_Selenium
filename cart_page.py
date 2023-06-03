from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.remove_items = ["//button[@data-test='remove-sauce-labs-backpack']", "", "", "", "", ""]
        """номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, 3 - Sauce Labs Bolt T-Shirt, 
                4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)"""


    def remove_product(self, item): # choose and add the product to the cart
        remove_product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_items[item-1])))
        remove_product.click()
        print("Click Remove Product")

