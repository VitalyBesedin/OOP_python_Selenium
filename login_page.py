from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):

        username = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@data-test='username']")))
        username.send_keys(login_name)
        print("Input login")
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))
        password.send_keys(login_password)
        print("Input password")
        button_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']")))
        button_login.click()
        print("Click login button")

    def cancel_wrong_login(self):
        button_red_cross = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.svg-inline--fa.fa-times.fa-w-11")))
        button_red_cross.click()
