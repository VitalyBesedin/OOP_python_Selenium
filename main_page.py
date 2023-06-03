from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.main_menu_items = ["","#react-burger-menu-btn","#logout_sidebar_link",""]

    def select_product(self, product_link): # choose and add the product to the cart

        select_product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, product_link)))
        select_product.click()
        print("Click Select Product")

    def click_enter_shopping_cart(self):
        enter_shopping_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='shopping_cart_badge']")))
        enter_shopping_cart.click()
        print("Click Enter Shopping Cart")

    def enter_item_main_menu(self, item):
        """items: 1 - All Items, 2 - About, 3 - Logout, 4 - Reset App State"""
        menu = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-burger-menu-btn")))
        menu.click()
        print("Click menu button")
        link_about = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_menu_items[item-1])))
        link_about.click()
        print("Click link menu")
