__author__ = 'sunny.yu2'
from behave import *
from PageModel.LoginPage import LoginPage
from features.accountManage import AccountManage


@given('I am a teacher')
def step_impl(context):
 loginPage = LoginPage()
 loginPage.userName(AccountManage.userName)
 loginPage.password(AccountManage.password)
 loginPage.signIn()


@given('this is "{text}" environment')
def step_impl(context,text):
 pass


@when('load some "{text}" arguments')
def step_impl(context,text):
  if(text=='qa'):
   AccountManage()
  else:
   AccountManage('staging')

@then("i can open omni")
def step_impl(context):
    context.basePage.openUrl(AccountManage.url)