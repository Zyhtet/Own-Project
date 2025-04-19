import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Day3:
    driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        print("T1: Done opening browser")
        time.sleep(1)

    def input(self):

        user_data = ("Ella","ee12@gmail.com","+66957573470")
        Link=self.driver.find_elements(By.CSS_SELECTOR, 'input[placeholder^="Enter"]')
        for i in range (len(user_data)):
            Link[i].send_keys(user_data[i])
            time.sleep(1)
            print("T2: Input Data Success")

    def address(self):
        self.driver.find_element(By.ID, 'textarea').send_keys('Yay /Myanmar/223 /QC St')
        time.sleep(1)
        print("T3: Input Address Success")

    def gender(self):
        self.driver.find_element(By.ID, 'male').click()
        time.sleep(1)
        print("T4: Click Gender Success")

    def day(self):
        day = ['monday','wednesday','thursday','friday','saturday']

        for i in range(len(day)):
            self.driver.find_element(By.ID, day[i]).click()
            time.sleep(2)
        print("T5: Day click Success")

    def country(self):
        Select(self.driver.find_element(By.ID, 'country')).select_by_value('china')
        time.sleep(1)
        print("T6: Country click Success")

    def multi_select(self):
        colour = self.driver.find_element(By.ID, 'colors')
        Select(colour).select_by_value('red')
        time.sleep(3)
        print("T7: Colour click Success")

        colour = self.driver.find_element(By.ID, 'animals')
        Select(colour).select_by_value('lion')
        time.sleep(1)
        Select(colour).select_by_value('zebra')
        print("T7: Colour click Success")
        time.sleep(3)

    def date(self):
        self.driver.find_element(By.ID, 'txtDate').click()
        time.sleep(1)
        print("T8: Date click Success")

        #yy
        Select(self.driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select[2]')).select_by_value('2022')
        time.sleep(1)

        #mm
        #Select(self.driver.find_element(By.CLASS_NAME, 'ui-datepicker-month')).select_by_value('5')
        #time.sleep(1)
        #dd
        #Select(self.driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[2]/a'))
        #time.sleep(3)
        print("T9: Date picking Success")

    def main(self):
        self.open_browser()
        self.input()
        self.address()
        self.gender()
        self.day()
        self.country()
        self.multi_select()
        self.date()

Day3().main()





