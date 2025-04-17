import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.common.action_chains import ActionChains



class Day5b:

    driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        print("T1: Done opening browser")
        time.sleep(2)

    def start_stop(self):
        self.driver.find_element(By.NAME, 'start').click()
        time.sleep(3)
        self.driver.find_element(By.NAME, 'stop').click()
        time.sleep(3)
        print("T2: Done clicking start/stop button")


    def alert_message(self):
        self.driver.find_element(By.ID, 'alertBtn').click()
        time.sleep(3)

     #confirmation(self):

        confirmation = self.driver.find_element(By.ID, 'confirmBtn')
        confirmation.click()
        time.sleep(3)


        alert = self.driver.switch_to.alert
        time.sleep(4)
        alert.dismiss()
        time.sleep(3)

        result = self.driver.find_element(By.ID, 'demo').text
        print(result)
        time.sleep(3)
        print("T3: Done alert")

        #window handle
    def handle(self):
        self.driver.find_element(By.XPATH, '//*[@id="PopUp"]').click()
        handle = self.driver.window_handles[0]
        time.sleep(3)
        self.driver.switch_to.window(handle)
        time.sleep(3)
        print("T4: Done handle")

    def field(self):
        field = self.driver.find_element(By.ID, 'field1')
        field.clear()
        time.sleep(3)
        field.send_keys("Zaw Ye")

        text_copy = self.driver.find_element(By.XPATH, '//*[@id="field2"]')
        action_chain = ActionChains(self.driver)
        action_chain.double_click(text_copy).perform()
        time.sleep(3)

        field2 = self.driver.find_element(By.ID,'field2').get_attribute('value')
        print(field2)
        time.sleep(3)
        print("T5: Done field2")

    def drag_and_drop(self):
        draggable = self.driver.find_element(By.ID, 'draggable')
        droppable = self.driver.find_element(By.ID, 'droppable')
        time.sleep(4)
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, droppable).perform()
        time.sleep(4)
        print("T6: Done draggable")













    def main(self):
        self.open_browser()
        self.start_stop()
        self.handle()
        self.field()
        self.drag_and_drop()

Day5b().main()
