__author__ = 'sunny.yu2'
from behave import *
from PageModel.BasePage import BasePage
from PageModel.GroupPage import GroupPage
from PageModel.AttendancePage import AttendancePage

def _init_(context):
   context.basePage = BasePage()
   context.groupPage = GroupPage()
   context.attendancePage=AttendancePage()

@when(u'I go to mark attendance {view}')
def step_impl(context, view):
   _init_(context)
   context.basePage.Loadfinish()
   context.groupPage.markAttendanceTab()
   if(view=='Course'):
      context.attendancePage.markAttendanceViewClick()

@then(u'I can check the students attendance info')
def step_impl(context):
   context


