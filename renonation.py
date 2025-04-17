from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time


class Own:
    def __init__(self):
        self.driver = webdriver.Firefox()

    #browser_opening
    def open_browser(self):
        self.driver.get("https://www.renonation.sg/")
        self.driver.maximize_window()
        print("Test1: Done opening browser")
        time.sleep(2)

    def free_quote(self):
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/header/div/div[2]/div/button[1]').click()
        time.sleep(2)
        print("Test2: Done free quote")


        #Properties type
        self.driver.find_element(By.CSS_SELECTOR, 'button[value="96e5ac2c-0e5f-11ee-a91a-0a0b69d58be8"]').click()
        time.sleep(2)
        print("Test3: Done selecting properties type")

        #1bed room
        self.driver.find_element(By.CSS_SELECTOR, 'button[value="6"]').click()
        time.sleep(2)
        print("Test4: Done selecting 1 bed room")


    def main(self):
        self.open_browser()
        self.free_quote()



Own().main()



