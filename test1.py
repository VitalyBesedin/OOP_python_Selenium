import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFirst:
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
        # time.sleep(5)

        print("Start test")
        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        username = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-test='username']")))
        username.send_keys(login_standard_user)
        print("Input login")
        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))
        password.send_keys(password_all)
        print("Input password")
        button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']")))
        button_login.click()
        print("Click login button")
        time.sleep(2)
        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click Select Product")
        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='shopping_cart_badge']")))
        enter_shopping_cart.click()
        print("Click Enter Shopping Cart")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        print(value_success_test)
        assert value_success_test == "Your Cart"
        print("Test Success")




        time.sleep(5)



test = TestFirst()
test.test_select_product()

