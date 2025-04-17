import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class Test:
    driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get("https://www.saucedemo.com/v1/index.html")
        print("done opening browser")
        self.driver.maximize_window()
        time.sleep(2)

    def login_username(self):
        self.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        time.sleep(3)

    def login_password(self):
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(3)

    def full_login(self):
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        time.sleep(3)

    def check_url(self):
        expected = 'https://www.saucedemo.com/v1/inventory.html'
        assert self.driver.current_url == expected
        print("url passed")

    def add(self):
        self.driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[3]/button').click()
        time.sleep(3)

    def cart(self):
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)

    def out(self):
        self.driver.find_element(By.XPATH,'//*[@id="cart_contents_container"]/div/div[2]/a[2]').click()
        time.sleep(3)

    def username(self):
        self.driver.find_element(By.ID, "first-name").send_keys("standard_user")
        time.sleep(3)

    def lastname(self):
        self.driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("secret_sauce")
        time.sleep(3)

    def code(self):
        self.driver.find_element(By.ID, "postal-code").send_keys("155")
        time.sleep(3)

    def final(self):
        self.driver.find_element(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/input').click()
        time.sleep(3)
        print("All success")

    def main(self):
        self.open_browser()
        self.login_username()
        self.login_password()
        self.full_login()
        self.check_url()
        self.add()
        self.cart()
        self.out()
        self.username()
        self.lastname()
        self.code()
        self.final()

Test().main()