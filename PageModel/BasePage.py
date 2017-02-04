__author__ = 'sunny.yu2'
from Browser.BrowserManage import BrowserManage
from WebElement.By import By
from Utilitys.Utils import Utils

class BasePage():

  def __init__(self):
    browserManage= BrowserManage()
    self.browser = browserManage.setBrowser()

  def title(self):
     self.browser.get_title()


  def openUrl(self,url):
      self.browser.open(url)

  def clearDriver(self):
      BrowserManage.browsers=None