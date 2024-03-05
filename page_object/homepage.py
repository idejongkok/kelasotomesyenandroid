from appium.webdriver.common.appiumby import AppiumBy
from locators.home_locator import HomeLocator

class Homepage:
    
    def __init__(self,driver):
        self.driver = driver
        
    def click_login_button(self):
        self.driver.find_element(AppiumBy.XPATH,HomeLocator.login_button).click()

