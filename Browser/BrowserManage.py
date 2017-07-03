
from Browser.Browser import Browser

__author__ = 'sunny.yu2'

class BrowserManage:
    browsers = None
    @staticmethod
    def setBrowser(envir="chrome"):
         if BrowserManage.browsers==None:
             if(envir=="chrome"):
                BrowserManage.browsers = Browser()

         return BrowserManage.browsers

    def clearBrowser(self):
             BrowserManage.browsers=None

