__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By

class GroupPage(BasePage):

 def markAttendanceTab(self):
    self.browser.find_web_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div[3]')