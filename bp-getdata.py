from subprocess import TimeoutExpired
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep  
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import Select
import difflib
import requests
from datetime import date, timedelta
import json
from types import SimpleNamespace


PATH = "C:/Users/Administrator/Documents/PY/chromedriver.exe"
driver = webdriver.Chrome(PATH)

def loginBp():
    driver.get("https://my.boldprime.com/crm/performance-dashboard/financial/")

    userlogin = "boldprimelimited"
    userpasword = "B0ldAdm!n@123"

    userinput = driver.find_element(By.ID,'form_login__username')
    passwordinput = driver.find_element(By.ID,'form_login__password')

    userinput.send_keys(userlogin)
    passwordinput.send_keys(userpasword)

    loginbutton = driver.find_element(By.TAG_NAME,'button')

    loginbutton.click()

    driver.maximize_window()

    # driver.minimize_window()

def loginKp():
    driver.get("https://fx.katoprime.com/crm/performance-dashboard/financial/")

    userlogin = "Administrator"
    userpasword = "KLio9*&^LKP"

    userinput = driver.find_element(By.ID,'form_login__username')
    passwordinput = driver.find_element(By.ID,'form_login__password')

    userinput.send_keys(userlogin)
    passwordinput.send_keys(userpasword)

    loginbutton = driver.find_element(By.TAG_NAME,'button')

    loginbutton.click()

    driver.maximize_window()

    # driver.minimize_window()


def loginLp():
    driver.get("https://secure.lunarpips.com/crm/performance-dashboard/financial/")

    userlogin = "Adam"
    userpasword = "XeroPrime@123"

    userinput = driver.find_element(By.ID,'form_login__username')
    passwordinput = driver.find_element(By.ID,'form_login__password')

    userinput.send_keys(userlogin)
    passwordinput.send_keys(userpasword)

    loginbutton = driver.find_element(By.TAG_NAME,'button')

    loginbutton.click()

    driver.maximize_window()

    # driver.minimize_window()

def loginVf():
    driver.get("https://dashboard.vectraforex.com/crm/performance-dashboard/financial/")

    userlogin = "admin"
    userpasword = "4?bgWq[T"

    userinput = driver.find_element(By.ID,'form_login__username')
    passwordinput = driver.find_element(By.ID,'form_login__password')

    userinput.send_keys(userlogin)
    passwordinput.send_keys(userpasword)

    loginbutton = driver.find_element(By.TAG_NAME,'button')

    loginbutton.click()

    driver.maximize_window()

    # driver.minimize_window()




def getThisWeeksDataBp():
    
    driver.get("https://my.boldprime.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)      

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text

    today = date.today().strftime('%d-%m-%Y')
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')

    print('THIS WEEK',  thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"this_week",
        "client":"bp"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/apiforapp/ENuGdIJdMSRA45qJ2lL3", json=json)

    print(response.status_code)

def getYesterdaysDataBp():
    driver.get("https://my.boldprime.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(yesterday)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(yesterday)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('YESTERDAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json2 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"yesterday",
        "client":"bp"
    }
    json3a = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"yesterday_historical",
        "client":"bp",
        "date": yesterday
    }

    resget = requests.get("https://us-central1-bp-serverless.cloudfunctions.net/apiforhist")

    res = json.loads(resget.content, object_hook=lambda d: SimpleNamespace(**d))

    arr = []
    arr = [i.date for i in res]

    if yesterday in arr:
        print('duplicate entry')
    else:
        response_h = requests.post("https://us-central1-bp-serverless.cloudfunctions.net/apiforhist", json=json3a)
        print(response_h.status_code)

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/apiforapp/6WCoEDwBcUVHEe9H804t", json=json2)

    print(response.status_code)

def getTodaysDataBp():
    driver.get("https://my.boldprime.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    todaymonth = date.today()
    thismonth = todaymonth.strftime("%B")
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(today)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(today)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('TODAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json3 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"today",
        "client":"bp"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/apiforapp/WHKD6X8a0FlNoSrHbj0z", json=json3)
    
    

    print(response.status_code)

def getMonthsDataBp():
    driver.get("https://my.boldprime.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    startMonth = (date.today() - timedelta(1)).strftime('1-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(startMonth)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(today)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('TODAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, startMonth)

    json4 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"this_Month",
        "client":"bp"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/apiforapp/MMOjWE4VH4XvEe1i9IkY", json=json4)
    

    print(response.status_code)

def getThisWeeksDataKp():
    
    driver.get("https://fx.katoprime.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)      

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text

    today = date.today().strftime('%d-%m-%Y')
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')

    print('THIS WEEK',  thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"this_week",
        "client":"kp"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/kp_apiforapp/6QzumaCIugKA6rdsJ7MD", json=json)

    print(response.status_code)

def getYesterdaysDataKp():
    driver.get("https://fx.katoprime.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(yesterday)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(yesterday)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('YESTERDAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json2 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"yesterday",
        "client":"kp"
    }
    json3a = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"yesterday_historical",
        "client":"kp",
        "date": yesterday
    }

    resget = requests.get("https://us-central1-bp-serverless.cloudfunctions.net/kp_apiforhist/")

    res = json.loads(resget.content, object_hook=lambda d: SimpleNamespace(**d))

    arr = []
    arr = [i.date for i in res]

    if yesterday in arr:
        print('duplicate entry')
    else:
        response_h = requests.post("https://us-central1-bp-serverless.cloudfunctions.net/kp_apiforhist", json=json3a)
        print(response_h.status_code)

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/kp_apiforapp/GlNOEvn3BbuYCixcbtFl", json=json2)

    print(response.status_code)

def getTodaysDataKp():
    driver.get("https://fx.katoprime.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    todaymonth = date.today()
    thismonth = todaymonth.strftime("%B")
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(today)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(today)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('TODAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json3 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"today",
        "client":"kp"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/kp_apiforapp/Hf8kIgl75t799jxOCyN5", json=json3)
    
    

    print(response.status_code)

def getMonthsDataKp():
    driver.get("https://fx.katoprime.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    startMonth = (date.today() - timedelta(1)).strftime('1-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(startMonth)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(today)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('TODAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, startMonth)

    json4 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"this_Month",
        "client":"kp"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/kp_apiforapp/l5UrDeIzFm7gtf2PSIFa", json=json4)
    

    print(response.status_code)


def getThisWeeksDataLp():
    
    driver.get("https://secure.lunarpips.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)      

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text

    today = date.today().strftime('%d-%m-%Y')
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')

    print('THIS WEEK',  thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"this_week",
        "client":"lp"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/lp_apiforapp/8hz0VufDteuzKIRKyIMp", json=json)

    print(response.status_code)

def getYesterdaysDataLp():
    driver.get("https://secure.lunarpips.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(yesterday)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(yesterday)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('YESTERDAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json2 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"yesterday",
        "client":"lp"
    }
    json3a = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"yesterday_historical",
        "client":"lp",
        "date": yesterday
    }

    resget = requests.get("https://us-central1-bp-serverless.cloudfunctions.net/lp_apiforhist/")

    res = json.loads(resget.content, object_hook=lambda d: SimpleNamespace(**d))

    arr = []
    arr = [i.date for i in res]

    if yesterday in arr:
        print('duplicate entry')
    else:
        response_h = requests.post("https://us-central1-bp-serverless.cloudfunctions.net/lp_apiforhist", json=json3a)
        print(response_h.status_code)

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/lp_apiforapp/A6Yrveceo3mGzbXMuoFq", json=json2)

    print(response.status_code)

def getTodaysDataLp():
    driver.get("https://secure.lunarpips.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    todaymonth = date.today()
    thismonth = todaymonth.strftime("%B")
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(today)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(today)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('TODAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json3 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"today",
        "client":"lp"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/lp_apiforapp/X3pzXKGKsN0UtcvJRxOW", json=json3)
    
    

    print(response.status_code)

def getMonthsDataLp():
    driver.get("https://secure.lunarpips.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    startMonth = (date.today() - timedelta(1)).strftime('1-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(startMonth)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(today)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('TODAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, startMonth)

    json4 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"this_Month",
        "client":"Lp"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/lp_apiforapp/fBqvQ04AhswlOeQJT6yL", json=json4)
    

    print(response.status_code)

def getThisWeeksDataVf():
    
    driver.get("https://dashboard.vectraforex.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)      

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text

    today = date.today().strftime('%d-%m-%Y')
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')

    print('THIS WEEK',  thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"this_week",
        "client":"vf"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/vf_apiforapp/Q9fWadDJ0xCkX4lJAffT", json=json)

    print(response.status_code)

def getYesterdaysDataVf():
    driver.get("https://dashboard.vectraforex.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(yesterday)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(yesterday)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('YESTERDAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json2 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"yesterday",
        "client":"vf"
    }
    json3a = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"yesterday_historical",
        "client":"vf",
        "date": yesterday
    }

    resget = requests.get("https://us-central1-bp-serverless.cloudfunctions.net/vf_apiforhist/")

    res = json.loads(resget.content, object_hook=lambda d: SimpleNamespace(**d))

    arr = []
    arr = [i.date for i in res]

    if yesterday in arr:
        print('duplicate entry')
    else:
        response_h = requests.post("https://us-central1-bp-serverless.cloudfunctions.net/vf_apiforhist", json=json3a)
        print(response_h.status_code)

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/vf_apiforapp/aH1p9EFjuWYT08lQ4nRl", json=json2)

    print(response.status_code)

def getTodaysDataVf():
    driver.get("https://dashboard.vectraforex.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    todaymonth = date.today()
    thismonth = todaymonth.strftime("%B")
    yesterday = (date.today() - timedelta(1)).strftime('%d-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(today)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(today)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('TODAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, yesterday)

    json3 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"today",
        "client":"vf"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/vf_apiforapp/hACn7UKPGOo7W6CQxLXS", json=json3)
    
    

    print(response.status_code)

def getMonthsDataVf():
    driver.get("https://dashboard.vectraforex.com/crm/performance-dashboard/financial/")

    wait = WebDriverWait(driver, 5)

    today = date.today().strftime('%d-%m-%Y')
    startMonth = (date.today() - timedelta(1)).strftime('1-%m-%Y')     

    cog = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div[1]/a') 

    cog.click()

    sleep(5)

    # fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')

    # fromdate.click()

    # fromdate.send_keys(Keys.CONTROL + "a")
    # fromdate.send_keys(Keys.DELETE)

    # fromdate.send_keys(yesterday)
    # try:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="from"]')))
    # except TimeoutExpired:
    #     fromdate = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="from"]')))
    try:
        fromdate = driver.find_element(By.XPATH, '//*[@id="from"]')
    except NoSuchElementException:
        fromdate = driver.find_element(By.XPATH, '//*[@name="from"]')

    fromdate.click()
    fromdate.send_keys(Keys.CONTROL + "a")
    fromdate.send_keys(startMonth)

    try:
        todate = driver.find_element(By.XPATH, '//*[@id="to"]')
    except NoSuchElementException:
        todate = driver.find_element(By.XPATH, '//*[@name="to"]')

    # todate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="to"]')))
    todate.click()
    todate.send_keys(Keys.CONTROL + "a")
    todate.send_keys(today)


    clickout = driver.find_element(By.CLASS_NAME, 'modal-header')

    clickout.click()

    submitdate = driver.find_element(By.XPATH, '//*[@id="submit"]')

    submitdate.click()

    wait = WebDriverWait(driver, 5)

    thisweeksDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[1]/div/h5').text
    thisweeksWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[2]/div/h5').text
    averageDP = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[3]/div/h5').text
    averageWD = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[4]/div/h5').text
    tpnl = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[5]/div/h5').text
    awd = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div/div/div[6]/div/h5').text


    print('TODAY', thisweeksDP, thisweeksWD, averageDP, averageWD, tpnl, awd, today, startMonth)

    json4 = {
        "this_tf_deposit": thisweeksDP,
        "this_tf_withdraw": thisweeksWD,
        "average_dp": averageDP,
        "average_wd": averageWD,
        "tpnl": tpnl, 
        "awd": awd,
        "timeframe":"this_Month",
        "client":"vf"
    }

    response = requests.put("https://us-central1-bp-serverless.cloudfunctions.net/vf_apiforapp/ys8yJmJaF8j9SeC9Ncfr", json=json4)
    

    print(response.status_code)    

loginBp()
loginKp()
loginLp()
loginVf()

while True:
    # driver.minimize_window()
    getMonthsDataBp()
    getThisWeeksDataBp()
    getYesterdaysDataBp()
    getTodaysDataBp()

    getMonthsDataKp()
    getThisWeeksDataKp()
    getYesterdaysDataKp()
    getTodaysDataKp()

    getMonthsDataLp()
    getThisWeeksDataLp()
    getYesterdaysDataLp()
    getTodaysDataLp()

    getMonthsDataVf()
    getThisWeeksDataVf()
    getYesterdaysDataVf()
    getTodaysDataVf()
    sleep(3600) 


    
    
    