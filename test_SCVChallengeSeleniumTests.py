import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSCVChallengeSeleniumTests():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='https://glacial-reef-23457.herokuapp.com/', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sCVChallengeSeleniumTests(self):
    # Test name: SCV_Challenge_Selenium_Tests
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://glacial-reef-23457.herokuapp.com/")
    # 2 | setWindowSize | 1936x1048 | 
    self.driver.set_window_size(1936, 1048)
    # 3 | click | css=.my-investments__title | 
    self.driver.find_element(By.CSS_SELECTOR, ".my-investments__title").click()
    # 4 | click | css=.my-investments__list:nth-child(5) .my-investments__items__name | 
    self.driver.find_element(By.CSS_SELECTOR, ".my-investments__list:nth-child(5) .my-investments__items__name").click()
    # 5 | click | css=.my-investments__list:nth-child(6) .my-investments__items__name | 
    self.driver.find_element(By.CSS_SELECTOR, ".my-investments__list:nth-child(6) .my-investments__items__name").click()
    # 6 | click | css=.my-investments__list:nth-child(7) .my-investments__items__name | 
    self.driver.find_element(By.CSS_SELECTOR, ".my-investments__list:nth-child(7) .my-investments__items__name").click()
    # 7 | click | css=div:nth-child(4) > input | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > input").click()
    # 8 | type | css=div:nth-child(4) > input | 050
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > input").send_keys("050")
    # 9 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # 10 | click | css=div:nth-child(5) > input | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > input").click()
    # 11 | type | css=div:nth-child(5) > input | 020
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > input").send_keys("020")
    # 12 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # 13 | mouseOver | css=.other-investments__list:nth-child(3) .other-investments__items__value | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".other-investments__list:nth-child(3) .other-investments__items__value")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 14 | mouseOver | css=.my-investments__title | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".my-investments__title")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 15 | click | css=.my-investments__title | 
    self.driver.find_element(By.CSS_SELECTOR, ".my-investments__title").click()
    # 16 | mouseOut | css=.my-investments__title | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
