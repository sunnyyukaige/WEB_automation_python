from behave import *

@then(u'I can go to group dashboard page successfully')
def step_impl(context):
    assert context.groupdashboardPage.checkGroupDetailsExist()
