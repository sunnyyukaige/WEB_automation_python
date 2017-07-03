__author__ = 'sunny.yu2 & sophia.lee'
from Browser.BrowserManage import BrowserManage
from WebElement.By import By
from WebElement.Waitor import Waitor
import time

class BasePage():

  def __init__(self):
    browserManage= BrowserManage()
    self.browser = browserManage.setBrowser()

  def title(self):
     self.browser.get_title()

  def Loadfinish(self):
      pass
       #time.sleep(2)
       #LoadFinish = self.browser.find_web_element(By.CLASS_NAME, '  pace-done')
       #Waitor.exist(LoadFinish)
       #time.sleep(5)


  def openUrl(self,url):
      self.browser.open(url)

  def clearDriver(self):
      BrowserManage.browsers=None