from logging import exception
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



PATH = "C:/Users/Administrator/Documents/PY/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://my.boldprime.com/crm/transactions/")

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

while True:
    driver.get("https://my.boldprime.com/crm/transactions/")

    # driver.minimize_window()

    statusinput = driver.find_element(By.XPATH, '//*[@id="form_col_transaction_status_55445945e0e5b28d39db5d975da414ee"]/div')
    tagsinput = driver.find_element(By.XPATH, '//*[@id="form_col_generalinfo_tags_09856735a17a8c7d3ebb945e8a925a87"]/div')
    notin = driver.find_element(By.XPATH, '//*[@id="form_col_generalinfo_tags_09856735a17a8c7d3ebb945e8a925a87_searchType_1"]')
    dummywd = driver.find_element(By.XPATH, '//*[@id="form_col_generalinfo_tags_09856735a17a8c7d3ebb945e8a925a87"]/div/div/div[3]/ul/li[8]')
    highrisk = driver.find_element(By.XPATH, '//*[@id="form_col_generalinfo_tags_09856735a17a8c7d3ebb945e8a925a87"]/div/div/div[3]/ul/li[10]')
    pendingbalres = driver.find_element(By.XPATH, '//*[@id="form_col_generalinfo_tags_09856735a17a8c7d3ebb945e8a925a87"]/div/div/div[3]/ul/li[11]')
    pendingbalres2 = driver.find_element(By.XPATH, '//*[@id="form_col_generalinfo_tags_09856735a17a8c7d3ebb945e8a925a87"]/div/div/div[3]/ul/li[13]')
    tier3 = driver.find_element(By.XPATH, '//*[@id="form_col_generalinfo_tags_09856735a17a8c7d3ebb945e8a925a87"]/div/div/div[3]/ul/li[18]')
    typeinput = driver.find_element(By.XPATH, '//*[@id="form_col_transaction_type_6271ac97415c8c9d9414f5ea27674df8"]/div/button')
    withdrawaltype = driver.find_element(By.XPATH, '//*[@id="form_col_transaction_type_6271ac97415c8c9d9414f5ea27674df8"]/div/div/div[3]/ul/li[21]')
    # firstenc = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/form/div[1]/div[3]/table/tbody/tr[1]/td[1]')
    easelect = driver.find_element(By.XPATH, '//*[@id="form_col_generalinfo_tags_09856735a17a8c7d3ebb945e8a925a87"]/div/div/div[3]/ul/li[9]/a/label/input')
    paymentsys = driver.find_element(By.XPATH, '//*[@id="form_col_transaction_paymentsystem_a7855dee4c9dd77670d2f178fbc3bb5a"]/div/button')
    lb1 = driver.find_element(By.XPATH, '//*[@id="form_col_transaction_paymentsystem_a7855dee4c9dd77670d2f178fbc3bb5a"]/div/div/div[3]/ul/li[15]/a/label/input')
    amt = driver.find_element(By.XPATH, '//*[@id="form_col_transaction_processedamount_1210d5280236e6ab9a2cb6ca8f74b1bb"]/input')
    lessthan = driver.find_element(By.XPATH, '//*[@id="form_col_transaction_processedamount_1210d5280236e6ab9a2cb6ca8f74b1bb"]/div/ul/li[3]')
    curr = driver.find_element(By.XPATH, '//*[@id="form_col_transaction_processedcurrency_01d4fdb1c233d2a34f0b248a4fbc4cfa"]/input')


    typeinput.click()

    withdrawaltype.click()

    statusinput.click()

    selection_status = driver.find_element(By.XPATH, '//*[@id="form_col_transaction_status_55445945e0e5b28d39db5d975da414ee"]/div/div/div[3]/ul/li[5]')

    selection_status.click()

    selection_submit = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/form/div[1]/div[1]/div/button[1]')

    tagsinput.click()

    notin.click()

    dummywd.click()

    highrisk.click()
    easelect.click()
    pendingbalres.click()
    pendingbalres2.click()

    # tier3.click()   

    amt.click()

    lessthan.click()

    amt.send_keys('-500.01')

    curr.click()

    curr.send_keys('USD')

    paymentsys.click()

    lb1.click()

    selection_submit.click()

    wait = WebDriverWait(driver, 5)       

    while True:
        try:
            element = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/form/div[1]/div[4]/table/tbody/tr[1]/td[2]/a')
            clientName = driver.find_element(By.XPATH, "/html/body/div/div/section[2]/form/div[1]/div[4]/table/tbody/tr[1]/td[8]/a").text  

            if element:
                print('found')
                break
            else:
                print('no new request')
                driver.refresh()
                sleep(60)
        except NoSuchElementException:
            print('ERROR CONT')
            driver.refresh()
            sleep(60)

    print('_____________next____________')
    sleep(2)
    element.click()


    first_link = driver.find_element(By.XPATH, "//a[contains(@href, '/crm/wallets/')]")

    main_window = driver.current_window_handle

    first_link.send_keys(Keys.CONTROL + Keys.RETURN)


    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.TAB)

    driver.switch_to.window(driver.window_handles[1])

    try:
        swift = driver.find_element(By.XPATH, '//*[@id="home"]/div/div/div/div[2]/table/tbody/tr[16]/td[2]').text
    except NoSuchElementException:
        swift = driver.find_element(By.XPATH, '//*[@id="home"]/div/div/div/div[2]/table/tbody/tr[10]/td[2]').text

    try:
        detectIDR = driver.find_element(By.XPATH, '//*[@id="home"]/div/div/div/div[2]/table/tbody/tr[4]/td[2]').text
        innerIDR = len(detectIDR)

        if (innerIDR > 0):
            print('success')
            selected_currencybank = detectIDR
        else:
            print('fail')
    except NoSuchElementException:
        print('no IDR')

    try:
        detectINR = driver.find_element(By.XPATH, '//*[@id="home"]/div/div/div/div[2]/table/tbody/tr[5]/td[2]').text
        ifsc = driver.find_element(By.XPATH, '//*[@id="home"]/div/div/div/div[2]/table/tbody/tr[11]/td[2]').text
        innerINR = len(detectINR)

        if (innerINR > 0):
            print('success')
            selected_currencybank = detectINR
            swift = ifsc
        else:
            print('fail')
    except NoSuchElementException:
        print('no INR') 

    try:
        detectMYR = driver.find_element(By.XPATH, '//*[@id="home"]/div/div/div/div[2]/table/tbody/tr[6]/td[2]').text
        innerMYR = len(detectMYR)
        if (innerMYR > 0):
            print('success')
            selected_currencybank = detectMYR
        else:
            print('fail')
    except NoSuchElementException:
        print('no MYR') 

    try:
        detectTHB = driver.find_element(By.XPATH, '//*[@id="home"]/div/div/div/div[2]/table/tbody/tr[7]/td[2]').text
        innerTHB = len(detectTHB)
        if (innerTHB > 0):
            print('success')
            selected_currencybank = detectTHB
        else:
            print('fail')
    except NoSuchElementException:
        print('no THB') 

    clientNameProof = driver.find_element(By.XPATH, '//*[@id="home"]/div/div/div/div[2]/table/tbody/tr[13]/td[2]').text


    driver.close()

    driver.switch_to.window(main_window)

    # approveStep1 = driver.find_element(By.CLASS_NAME, 'btn-success')

    declineStep1 = driver.find_element(By.CLASS_NAME, 'btn-danger')

    print(clientName,clientNameProof.lower())

    def pos_route():
       
        apprv = driver.find_element(By.XPATH, "//a[text()[contains(., 'Approve')]]")
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        apprv.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())

        driver.switch_to.alert.accept()

        try:
            approveStep2v2 = driver.find_element(By.XPATH, "//a[contains(@href, '/approve')]")
        except NoSuchElementException:
            approveStep2v2 = driver.find_element(By.XPATH, "//a[contains(@href, '/vendor')]")
        

        approveStep2v2.click()

        WebDriverWait(driver, 10).until(EC.alert_is_present())

        driver.switch_to.alert.accept()
        
        ctnBtn = driver.find_element(By.XPATH, '//*[@id="form_transaction_approve_submit"]')

        ctnBtn.click()
        
        processBtn = driver.find_element(By.XPATH, "//a[contains(@href, '/vendor')]")

        processBtn.click()

        WebDriverWait(driver, 10).until(EC.alert_is_present())


        driver.switch_to.alert.accept()
        
        bankCodeInput = driver.find_element(By.XPATH, '//*[@id="form_transaction_vendor_data_bankCode"]')

        bankCodeInput.send_keys(swift)
        
        lastbtn = driver.find_element(By.XPATH, '//*[@id="form_transaction_vendor_submit"]')
        
        bankName = driver.find_element(By.XPATH, '//*[@id="form_transaction_vendor_data_bankName"]').get_attribute("value")
        print('_____________next____________')
        print(bankName, 'input by client')
        print(detectMYR, 'dropdown by client')

        if ('maybank' in bankName.lower() or 'malayan' in bankName.lower() or 'mbb' in bankName.lower() or 'malaysia' in bankName.lower()):
            mbb_select = driver.find_element(By.XPATH, '//*[@id="form_transaction_vendor_data_bankCode"]')
            select = Select(driver.find_element(By.XPATH, '//*[@id="form_transaction_vendor_data_paymentOperator"]'))
            select.select_by_visible_text('Maybank')
        elif ('am bank' in selected_currencybank.lower() ):
            select = Select(driver.find_element(By.XPATH, '//*[@id="form_transaction_vendor_data_paymentOperator"]'))
            select.select_by_visible_text('AM Bank')
        else:
            # userBankInput = driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div/div/div/form/div[2]/div/div/div/div/div[1]/div[4]/div/div/div/input').text
            # bankChoices = driver.find_element(By.TAG_NAME, 'option')
            select2 = Select(driver.find_element(By.XPATH, '//*[@id="form_transaction_vendor_data_paymentOperator"]'))

            print(selected_currencybank)

            option = [x.text for x in select2.options]
            
            prem_a = option

            if selected_currencybank.lower() == 'cimb' or selected_currencybank.lower() == 'cimb bank':
                prem_b = selected_currencybank + 'Clicks'
                print(prem_b,'if')

                
            else:
                prem_b = selected_currencybank
                print(prem_b,'else')
            choice_array = sorted(prem_a, key=lambda x: difflib.SequenceMatcher(None, x, prem_b).ratio(), reverse=True)

            print(choice_array[0])
            select = Select(driver.find_element(By.XPATH, '//*[@id="form_transaction_vendor_data_paymentOperator"]'))
            select.select_by_visible_text(choice_array[0])

                    
            
            
        lastbtn.click()
        # driver.minimize_window()
    def neg_route(theName):
        
        declineStep1.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        print(theName)
        declinersn = driver.find_element(By.ID, 'form_transaction_decline_declineReason')
        part1 = "Please change payment details field: ACCOUNT NAME to"
        part2 = "Transaction unsuccessful due to invalid account name"
        declinersn.clear()
        declinersn.send_keys(part1 + "\n" + theName + "\n" + part2)

        declinesub = driver.find_element(By.XPATH, '//*[@id="form_transaction_decline_submit"]')

        declinesub.click()
        # driver.minimize_window()

    premise_a = clientNameProof.lower()
    premise_b = clientName.lower()

    temp = difflib.SequenceMatcher(None,premise_a ,premise_b)

    print(temp.ratio())

    rat = temp.ratio()

    if rat > 0.7:
        print(clientName, 'is correct')
        pos_route()
    else:
        neg_route(clientName)

    
    
    
