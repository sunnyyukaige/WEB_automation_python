__author__ = 'sunny.yu2'
from PageModel.BasePage import *
from PageModel.GroupPage import GroupPage
from PageModel.GroupdashboardPage import GroupdashboardPage
from PageModel.AttendancePage import AttendancePage
from features.accountManage import AccountManage

def _init_page(context):
   context.basePage = BasePage()
   context.groupPage = GroupPage()
   context.attendancePage = AttendancePage()
   context.groupdashboardPage=GroupdashboardPage()

def before_scenario(context,scenario ):
   tag=context.config.userdata['env']
   # if you want to debug just uncomment below line and comment above line
   #tag='qa'
   if (tag == 'qa'):
      AccountManage()
   else:
      AccountManage('staging')
   _init_page(context)
   context.basePage.openUrl(AccountManage.url)

def after_scenario(context, scenario):
   if(scenario.status=="failed"):
      logtime=str(time.time())+".png"
      context.basePage.browser.get_screenshot_as_file("../Result/"+logtime)
   context.basePage.browser.quit()
   context.basePage.clearDriver()

def before_tag(context,tag):
   pass

def after_tag(context,tag):
   pass





