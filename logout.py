import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Logout_Tugas_Day_17(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

     # Test Case Logout
    def testLogout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # open website
        driver.maximize_window()
        time.sleep(2)

        # fill valid username
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        time.sleep(1)

        # fill valid password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)


        # click Login button
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # click dropdown button
        driver.find_element(By.XPATH, "/html//button[@id='react-burger-menu-btn']").click()
        time.sleep(2)

        # click Logout button
        driver.find_element(By.XPATH, "/html//a[@id='logout_sidebar_link']").click()
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()