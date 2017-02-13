__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By

class GroupPage(BasePage):

 def markAttendanceTab(self):
    self.browser.find_web_element(By.CLASS_NAME,'test-button-go-to-attendance').click()
