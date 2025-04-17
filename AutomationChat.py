import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

class Chat:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        print("T1: Done opening browser")
        time.sleep(1)

    def start_stop(self):
        self.driver.find_element(By.NAME, 'start').click()
        time.sleep(3)
        self.driver.find_element(By.NAME, 'stop').click()
        time.sleep(3)
        print("T2: Done clicking start/stop button")

    def alert_message(self):
        # Click the alert button to open an alert
        self.driver.find_element(By.ID, 'alertBtn').click()
        time.sleep(2)

        # Handle the first alert
        try:
            alert = self.driver.switch_to.alert
            print(f"Alert Text: {alert.text}")  # Print alert message (optional)
            alert.accept()  # Accept the alert (click "OK")
            print("First alert handled")
        except NoAlertPresentException:
            print("No alert found!")

        time.sleep(2)

        # Now safely click the confirm button
        confirmation = self.driver.find_element(By.ID, 'confirmBtn')
        confirmation.click()
        time.sleep(2)

        # Handle the second confirmation alert
        try:
            alert = self.driver.switch_to.alert
            print(f"Confirmation Alert Text: {alert.text}")  # Print confirmation text (optional)
            alert.dismiss()  # Dismiss the alert (click "Cancel")
            print("Confirmation alert dismissed")
        except NoAlertPresentException:
            print("No confirmation alert found!")

        time.sleep(2)

        # Get the confirmation result text
        result = self.driver.find_element(By.ID, 'demo').text
        print(f"Result: {result}")
        print("T3: Done alert")

    def main(self):
        self.open_browser()
        self.start_stop()
        self.alert_message()

if __name__ == "__main__":
    Chat().main()
