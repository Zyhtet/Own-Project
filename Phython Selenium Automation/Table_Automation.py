import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Day5:

    driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        print("T1: Done opening browser")
        time.sleep(1)

    def pagination_table(self):

     for i in range (1,5):
         link = f'//*[@id="pagination"]/li[{i}]/a'
         self.driver.find_element(By.XPATH, link).click()
         time.sleep(3)

         table = self.driver.find_element(By.ID, 'productTable')
         rows = table.find_elements(By.TAG_NAME, 'tr')
         table_data = []
         for row in rows:
          cells = row.find_elements(By.TAG_NAME, 'td')
          table_data.append(cell.text for cell in cells)

         for row in table_data:
          print('\t'.join(row))
          print('='*55)
         time.sleep(4)
         print('T1 Loop Table Success')









    def main(self):
        self.open_browser()
        self.pagination_table()



Day5().main()