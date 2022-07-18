#coding=UTF-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait #等待讀取時使用
from selenium.webdriver.support import expected_conditions as EC #等待讀取時使用
import pytest
from selenium.webdriver.firefox.service import Service
import allure
#帳密記得清除
#--------------------------------------------測項1是否能搜尋指定商品---------------------------------------------------
@allure.step('打開網頁')
def openBrowser():
    path="./geckodriver"
    service = Service(path)
    driver=webdriver.Firefox(service=service)
    driver.get('https://www.myacg.com.tw/index.php')
    return driver
@allure.step("關閉網頁")
def closeBrowser(driver):
    driver.quit()
@allure.step("搜尋")
def search(driver):
    search=driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div[1]/form/input[2]')
    search.click()
    search.send_keys('中野三玖')
    search.send_keys(Keys.RETURN)
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[3]'))
    )
    time.sleep(5)
@allure.step("進階搜尋")
def search_evolution(driver):
    search_all=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[2]/div[1]/p[2]/select')   #全部物品
    search_all.click()
    search_toy=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[2]/div[1]/p[2]/select/option[2]') #玩具
    search_toy.click()
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[3]'))
    )
    search_evolution=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[2]/div[1]/div/input') #搜尋
    search_evolution.click()
@allure.step("預購商品")
def button_predict(driver):
    button_predict=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[3]/div[1]/a[3]') #預購
    button_predict.click()
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[4]/ul/li[5]/div[1]'))
    )
@allure.step("預購商品")
def button_commodity(driver):
    button_commodity=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[4]/ul/li[5]/div[2]/a') #預購商品
    button_commodity.click()
    handles = driver.window_handles
    for handle in handles:
        if handle != driver.current_window_handle:
            driver.close()
            driver.switch_to.window(handle)# 切换窗口
    WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div[5]'))
    )
    sleep(0.3)
@allure.step("抓字")
def getText(driver):
    listname1=driver.find_elements(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[2]/div[1]/div[1]/span[3]/h2')
    return listname1
@allure.step("驗證")
def verify(driver):
    print(getText(driver))
    for i in getText(driver):
        assert  "█Mine公仔█日版 五等分的新娘 GSC 中野三玖 Date Style 1/6 PVC 三玖 五等分的花嫁D1925" == i.text
@allure.story("搜尋測試")
def test_verify():     #需要執行的動作
    driver=openBrowser()
    search(driver)
    search_evolution(driver)
    button_predict(driver)
    button_commodity(driver)
    getText(driver)
    verify(driver)
    closeBrowser(driver)
# -------------------------測項2商品資訊是否正常顯示------------------------------------------------------------
@allure.step("商品")
def titles(driver):
    time.sleep(3)
    get_commodity=driver.find_elements(By.XPATH, '/html/body/div[7]/div[2]/div[4]/div[2]/div/div[1]/a')
    return get_commodity
@allure.step("驗證")
def verify_titles(driver):
    print(titles(driver))
    for i in titles(driver):
        assert  '█Mine公仔█' == i.text
@allure.story("測試商品資訊是否正常顯示")
def test_verify_titles():     #需要執行的動作
    driver=openBrowser()
    search(driver)
    search_evolution(driver)
    button_predict(driver)
    button_commodity(driver)
    xxx_text = titles(driver)
    verify_titles(driver)
    closeBrowser(driver)
# #-----------------測項3點登入測試------------------------------
@allure.step("登入")
def button_member(driver):
    member=driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[2]/a') #會員登入
    member.click()
@allure.step("輸入帳密")
def button_passowrd(driver):
    input_username=driver.find_element(By.XPATH, '/html/body/div[5]/form/div/div/div[2]/div[2]/input')
    input_username.click()
    input_username.send_keys('eo4')
    time.sleep(2)
    input_passowrd=driver.find_element(By.XPATH, '/html/body/div[5]/form/div/div/div[2]/div[3]/input')
    input_passowrd.click()
    input_passowrd.send_keys('e04')
    time.sleep(2)
@allure.step("登入")
def button_login(driver):
    login=driver.find_element(By.XPATH, '/html/body/div[5]/form/div/div/div[2]/div[5]/div[1]/a')
    login.click()
@allure.step("抓字")
def get_username(driver):
    listname2=driver.find_elements(By.XPATH, '/html/body/div[3]/div/div')
    return listname2
@allure.step("驗證")
def verify_login(driver):
    print(get_username(driver))
    for i in get_username(driver):
        assert  '會員 philipcrown 您好！' == i.text
@allure.story("登入測試")
def test_verify_login():     #需要執行的動作
    driver=openBrowser()
    button_member(driver)
    button_passowrd(driver)
    button_login(driver)
    get_username(driver)
    verify_login(driver)
    closeBrowser(driver)
# #---------------------------------測項4修改個人資訊-----------------------------------
@allure.step("個人資料")
def myself_data(driver):
    sell_data=driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li/a')#我的拍賣
    sell_data.click()
    myself_data=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[2]/div/ul/li[5]/a/b').click()
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)#頁面下滑
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    City=driver.find_element(By.XPATH, '//*[@id="address_county"]').click()
    City_button=driver.find_element(By.XPATH, '/html/body/div[7]/div[4]/div[2]/div[4]/div[2]/div[1]/ul[4]/li[2]/span[2]/span[1]/select/option[10]').click()
    address=driver.find_element(By.XPATH, '//*[@id="address_city"]').click()
    button_address=driver.find_element(By.XPATH, '/html/body/div[7]/div[4]/div[2]/div[4]/div[2]/div[1]/ul[4]/li[2]/span[2]/span[2]/select/option[7]').click()
    input_address=driver.find_element(By.XPATH, '//*[@id="address"]')
    input_address.clear()
    input_address.send_keys(Keys.CONTROL + 'a')
    input_address.send_keys(Keys.BACKSPACE)#清掉
    input_address.send_keys('景賢')
    time.sleep(3)

@allure.step("儲存")
def save(driver):
    save_buutton=driver.find_element(By.XPATH, "/html/body/div[7]/div[4]/div[2]/div[4]/div[2]/div[2]/a")
    save_buutton.click()
    driver.switch_to.alert.accept()
    time.sleep(3)
@allure.step('更改變化')
def city_change(driver):
    citytext=driver.find_element(By.XPATH, '//*[@id="address_zip"]')
    # return citytext.get_attribute('value')
    print(citytext.get_attribute('value'))
@allure.step("驗證")
def verify_change(driver):
    print(city_change(driver))
    for citytext in city_change(driver):
        assert  '406' == citytext.text
@allure.step('重製')
def reset(driver):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    City=driver.find_element(By.XPATH, '//*[@id="address_county"]').click()
    City_button=driver.find_element(By.XPATH, '/html/body/div[7]/div[4]/div[2]/div[4]/div[2]/div[1]/ul[4]/li[2]/span[2]/span[1]/select/option[3]').click()
    address=driver.find_element(By.XPATH, '//*[@id="address_city"]').click()
    button_address=driver.find_element(By.XPATH, '/html/body/div[7]/div[4]/div[2]/div[4]/div[2]/div[1]/ul[4]/li[2]/span[2]/span[2]/select/option[8]')
    input_address=driver.find_element(By.XPATH, '//*[@id="address"]')
    input_address.clear()
    input_address.send_keys(Keys.CONTROL + 'a')
    input_address.send_keys(Keys.BACKSPACE)#清掉
    save=driver.find_element(By.XPATH, "/html/body/div[7]/div[4]/div[2]/div[4]/div[2]/div[2]/a")
    save.click()
    driver.switch_to.alert.accept()
    
@allure.story("修改個人資訊")
def test_verify_change():    #需要執行的動作
    driver=openBrowser()
    button_member(driver)
    button_passowrd(driver)
    button_login(driver)
    myself_data(driver)
    save(driver)
    city_change(driver)
    verify_change(driver)
    reset(driver)
    closeBrowser(driver)
#----------------------------測項5問題討論的告知----------------
@allure.step("法律問題")
def contract(driver):
    driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/ul/li[7]/h4/a').click()
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    # driver.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
    # driver.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
@allure.step("法律")
def law(driver):
    get_law=driver.find_elements(By.XPATH, '/html/body/div[7]/div[3]/div[1]/dl[1]/dt')
    return get_law
@allure.step("驗證")
def verify_law(driver):
    print(law(driver))
    for lawtext in law(driver):
        assert  'Q1.買動漫是什麼樣的網站？是購物網站嗎？' == lawtext.text
@allure.story('法律問題')
def test_verify_law():
    driver=openBrowser()
    contract(driver)
    law(driver)
    verify_law(driver)
    closeBrowser(driver)