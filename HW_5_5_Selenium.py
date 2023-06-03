import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from main_page import MainPage


class TestHW:
    def test_select_product(self):
        user_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']

        for i in range(len(user_list)):

            print("Start test", i + 1)
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
            password_all = "secret_sauce"
            login = LoginPage(driver)
            login.authorization(user_list[i], password_all)

            try: # positive test
                success_login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".title")))
                value_success_login = success_login.text
                print(value_success_login)
                assert value_success_login == "Products"
                print("Login Success")
            except TimeoutException as exception: # negative test
                print("Login Unsuccessful")
                driver.quit()
                print("Test Success", i + 1)
                continue

            select_product = MainPage(driver)
            select_product.select_product("#add-to-cart-sauce-labs-backpack")
            select_product.click_enter_shopping_cart()
            success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
            value_success_test = success_test.text
            print(value_success_test)
            assert value_success_test == "Your Cart"
            print("Test Success", i + 1)
            time.sleep(2)
            driver.quit()

print("Start Set of Tests")
test = TestHW()
test.test_select_product()
time.sleep(5)
print("End Set of Tests")
