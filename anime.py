#coding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait #等待讀取時使用
from selenium.webdriver.support import expected_conditions as EC #等待讀取時使用

#-------------------------------------------------
from selenium.webdriver.firefox.service import Service
path="./geckodriver"
service = Service(path)
driver = webdriver.Firefox(service=service)
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑上面為Firefox的驅動開法

driver.get('https://www.myacg.com.tw/index.php')

# print(driver.title)#取得開頭標題

search=driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/div[1]/form/input[2]')
search.clear()
search.send_keys('中野三玖')
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[3]'))
)


sch1=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[2]/div[1]/p[2]/select')   #全部物品
sch1.click()

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[2]/div[1]/p[2]/select/option[5]'))
)

search2=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[2]/div[1]/p[2]/select/option[2]') #玩具
search2.click()
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[3]'))
)
search3=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[2]/div[1]/div/input') #搜尋
search3.click()
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[3]/div[1]/a[3]'))
)

search4=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[3]/div[1]/a[3]') #預購
search4.click()
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div[4]/ul/li[5]/div[1]'))
)

search5=driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div[4]/ul/li[5]/div[2]/a') #預購商品
search5.click()

#------------因有跳視窗的話控制權會留在原本的視窗，以下為轉移控制權的方法-----------------------

handles = driver.window_handles
for handle in handles:
    if handle != driver.current_window_handle:
        # print(‘切换窗口‘,handle,driver.current_url,driver.current_window_handle)
        driver.close()#關掉第一個視窗
        driver.switch_to.window(handle)# 切换窗口

#------------因有跳視窗的話控制權會留在原本的視窗，以上為轉移控制權的方法-----------------------

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div[5]'))
)

titles=driver.find_elements(By.XPATH, '/html/body/div[7]/div[3]')
for title in titles:
    print(title.text)

time.sleep(2)
search6=driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[2]/div[1]/div[3]/dl[7]/dd/div/a[1]') #直接購買
search6.click()


time.sleep(5)
driver.quit()
