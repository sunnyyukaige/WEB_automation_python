__author__ = 'sunny.yu2 & sophia.lee'
from behave import *

@when(u'I go to mark attendance {view}')
def step_impl(context, view):
   context.basePage.Loadfinish()
   context.groupPage.markAttendanceTab()
   if(view=='Course'):
      context.attendancePage.markAttendanceViewClick()
   else:
      pass

@when(u'I can mark {status} attendance in {view}')
def step_impl(context, status, view):
   context.basePage.Loadfinish()
   context.groupPage.markAttendanceTab()
   if (view == 'Course'):
      context.attendancePage.markAttendanceViewClick()
   else:
      pass
   context.attendancePage.doMarkAttendance(status, view)

@then(u'I can check the students attendance {status} in {view}')
def step_impl(context, status, view):
   assert context.attendancePage.checkStudentAttendanceInfo(status, view)

