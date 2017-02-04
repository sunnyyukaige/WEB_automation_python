__author__ = 'sunny.yu2'
from behave import *
from PageModel.BasePage import BasePage
from PageModel.GroupPage import GroupPage

def _init_(context):
   context.basePage = BasePage()
   context.groupPage = GroupPage()


@when(u'I go to mark attendance {view}')
def step_impl(context, view):
   _init_(context)
   context.groupPage.markAttendanceTab()

@then(u'I can check the students attendance info')
def step_impl(context):
   context


