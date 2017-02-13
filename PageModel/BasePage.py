__author__ = 'sunny.yu2'
from Browser.BrowserManage import BrowserManage
from WebElement.By import By
from Utilitys.Utils import Utils
import time

class BasePage():

  def __init__(self):
    browserManage= BrowserManage()
    self.browser = browserManage.setBrowser()

  def title(self):
     self.browser.get_title()

  def Loadfinish(self):
     time.sleep(5)

  def openUrl(self,url):
      self.browser.open(url)

  def clearDriver(self):
      BrowserManage.browsers=None