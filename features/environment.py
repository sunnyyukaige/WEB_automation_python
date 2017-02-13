__author__ = 'sunny.yu2'
from PageModel.BasePage import *
from features.accountManage import AccountManage



def before_scenario(context, scenario):
   AccountManage()
   context.basePage = BasePage()
   context.basePage.openUrl('http://omni-operation-qa.ef.cn/group/11010')


def after_scenario(context, scenario):

   context.basePage.browser.quit()
   context.basePage.clearDriver()


