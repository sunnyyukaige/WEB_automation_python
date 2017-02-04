from time import sleep

from behave import *
from PageModel.LoginPage import LoginPage
from features.accountManage import AccountManage


@given('I am a teacher')
def step_impl(context):
 loginPage = LoginPage()
 loginPage.userName(AccountManage.userName)
 loginPage.password(AccountManage.password)
 loginPage.signIn()
