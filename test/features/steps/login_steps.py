from behave import *
from selenium.webdriver.common.by import By
import time
import random
import string

@given(u'I am on the homepage')
def step_impl(context):
    context.browser.get("https://www.manutd.com") 
    time.sleep(5)
    context.browser.find_element(By.ID, "later").click() 
    assert(context.browser.title) == "Official Manchester United Website"
    #perubahan



@when(u'I cick sign in')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "span.user-signin").click()
    context.browser.find_element(By.XPATH, "//a[span='LOG IN']").click()
    #//*[@id="listbox2"]/li[1]/div/a/span[1] 
    #//a[span="LOG IN"]
    #//tamabahana
    

@when(u'I fill my credentials')
def step_impl(context):
    randomChar = random.choice(string.ascii_letters)
    time.sleep(5)
    # Scrol down after filling credentials
    context.browser.execute_script("window.scrollTo(10, document.body.scrollHeight);")
    context.browser.find_element(By.ID, "loginID").send_keys(randomChar + "@gmail.com")
    context.browser.find_element(By.ID, "password").send_keys("0213402359a")
    context.browser.find_element(By.XPATH, "//*[@id='gigya-login-form']/div[1]/div[3]/div[4]/input").click()
    time.sleep(5)
    
    

@then(u"I can't login with wrong credentials")
def step_impl(context):   
    context.browser.find_element(By.XPATH, " //div[text()='Please enter a valid email address or password']").is_displayed()