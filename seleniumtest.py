import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time


class SeleniumTests(unittest.TestCase):
    def setUp(self):

        # Do not display browser when testing
        options = ChromeOptions()
        options.add_argument("--headless=new")

        self.driver = None
        try:
            # self.driver = webdriver.Chrome(options=options)
            self.driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub", options=options)
            self.driver.set_page_load_timeout(10)
            self.driver.get(f"http://appurl:5000/")
            self.driver.implicitly_wait(1)
        except WebDriverException as e:
            self.driver.quit()
            print(e)

    def test_validate_pass(self):
        text_box = self.driver.find_element(By.NAME, "text_box")
        text_box.clear()
        text_box.send_keys("abcde12345")
        submit_button = self.driver.find_element(By.NAME, "submit_button")
        submit_button.click()

        self.driver.implicitly_wait(1)

        result = self.driver.find_element(By.ID, "validated_result")
        self.assertEqual(result.text, "abcde12345")
        result = len(self.driver.find_elements(By.NAME, "text_box"))
        self.assertEqual(result, 0)
        result = len(self.driver.find_elements(By.NAME, "submit_button"))
        self.assertEqual(result, 0)

    def test_validate_fail(self):
        text_box = self.driver.find_element(By.NAME, "text_box")
        text_box.clear()
        text_box.send_keys(r"abcd&><'\"efgh")
        submit_button = self.driver.find_element(By.NAME, "submit_button")
        submit_button.click()

        self.driver.implicitly_wait(1)

        result = len(self.driver.find_elements(By.XPATH, '//*[@id="validated_result"]'))
        self.assertEqual(result, 0)
        result = len(self.driver.find_elements(By.NAME, "text_box"))
        self.assertEqual(result, 1)
        result = len(self.driver.find_elements(By.NAME, "submit_button"))
        self.assertEqual(result, 1)
    def tearDown(self):
        self.driver.quit()


