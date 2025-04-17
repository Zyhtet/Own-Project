
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
class Demo:
    driver = webdriver.Edge()

    def open_browser(self):
        self.driver.get("https://www.saucedemo.com/")
        print("test1: browser successfully opened")
        self.driver.maximize_window()
        time.sleep(3)
    #driver.quit()

    def login(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        time.sleep(4)

        #click
        self.driver.find_element(By.NAME, 'login-button').click()

        #error
        result =  self.driver.find_element(By.TAG_NAME, 'h3').text
        print("need password:",result)

        #error close
        self.driver.find_element(By.CLASS_NAME, 'error-button').click()
        time.sleep(2)

        #password
        self.driver.find_element(By.NAME, 'password').send_keys('123')

        self.driver.find_element(By.NAME, 'login-button').click()

        result =  self.driver.find_element(By.TAG_NAME, 'h3').text
        print("password is wrong:",result)

        #error close
        self.driver.find_element(By.CLASS_NAME, 'error-button').click()
        time.sleep(2)

        #clear password
        self.driver.find_element(By.NAME, 'password').clear()
        time.sleep(2)

        #right password
        self.driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
        time.sleep(2)

        #again login
        self.driver.find_element(By.NAME, 'login-button').click()



    def verify_login(self):
        expected_url = "https://www.saucedemo.com/inventory.html"
        now_url = self.driver.current_url

        assert expected_url == now_url
        assert"Swag Labs"in self.driver.title
        print("login successful")

    def cart_view(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        time.sleep(2)

        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
        time.sleep(3)

    def main(self):
        self.open_browser()
        self.login()
        self.verify_login()
        self.cart_view()
        time.sleep(3)

Demo().main()