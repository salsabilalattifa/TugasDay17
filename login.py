import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_Tugas_Day_17(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # Test Case Login
    # Login using invalid username and invalid password
    def testLogin_Failed1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # open website
        driver.maximize_window()
        time.sleep(1)

        # fill invalid username
        driver.find_element(By.ID, "user-name").send_keys("cobacobacoba")
        time.sleep(1)

        # fill invalid password
        driver.find_element(By.ID, "password").send_keys("coba123456")
        time.sleep(1)

        # click Login button
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    # Login using using valid username and invalid password
    def testLogin_Faied2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # open website
        driver.maximize_window()
        time.sleep(1)

        # fill valid username
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        time.sleep(1)

        # fill invalid password
        driver.find_element(By.ID, "password").send_keys("1234")
        time.sleep(1)

        # click Login button
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    # Login using using invalid username and valid password
    def testLogin_Faied3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # open website
        driver.maximize_window()
        time.sleep(1)

        # fill invalid username
        driver.find_element(By.ID, "user-name").send_keys("usernamesalah")
        time.sleep(1)

        # fill valid password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)

        # click Login button
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    # Blank field
    def testLogin_Faied4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # open website
        driver.maximize_window()
        time.sleep(1)

        # click Login button
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    # Login success with valid username and valid password
    def testLogin_Success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # open website
        driver.maximize_window()
        time.sleep(1)

        # fill valid username
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)

        # fill valid password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)

        # click Login button
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()