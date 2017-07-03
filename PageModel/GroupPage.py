__author__ = 'sunny.yu2 & sophia.lee'
from PageModel.BasePage import BasePage
from WebElement.By import By
from WebElement.Waitor import Waitor
import time

class GroupPage(BasePage):

 def markAttendanceTab(self):
    self.browser.find_web_element(By.CLASS_NAME,'test-Attendance-link').click()
    #time.sleep(5)




