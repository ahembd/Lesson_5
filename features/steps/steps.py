from behave import given, then, when
from selenium.webdriver.common.by import By

@given('the user has a valid user name and password and the user has navigated to the Target web page')
def login(context):
    context.driver.get('https://www.target.com/')

@when('he clicks the Sign in button and then clicks username')
def click_signin(context):
    context.driver.find_element(By.ID, "headerPrimary").click()

@then('the process will log him in.')
def validate_log_in(context):
    context.driver.find_element(By.ID, 'headerPrimary').click()
    greeting = context.driver.find_element(By.XPATH, "//*[@id='headerPrimary']/a[4]").text
    print(f'Greeting = {greeting}')
    assert 'Sign in' in greeting, 'login was not successful'
