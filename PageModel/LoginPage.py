__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By


class LoginPage(BasePage):

 def userName(self,value):
    element=self.browser.find_web_element(By.ID,'username')
    element.clear()
    element.send_keys(value)

 def password(self,value):
     element=self.browser.find_web_element(By.NAME,'password')
     element.clear()
     element.send_keys(value)

 def signIn(self):
     element= self.browser.find_web_element(By.TAG_NAME,'button')
     element.click()