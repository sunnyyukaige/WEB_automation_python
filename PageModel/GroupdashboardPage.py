_author_='Susan.yao'
from PageModel.BasePage import BasePage
from WebElement.By import By

class GroupdashboardPage(BasePage):

 def checkGroupDetailsExist(self):
    isTrue=False
    self.browser.find_web_element(By.CLASS_NAME, 'test-group-detail-view')
    return isTrue