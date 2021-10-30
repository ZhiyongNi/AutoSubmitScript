# 本地Chrome浏览器设置方法

from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://20.3.237.1:7001/fund-capital/standard/')
time.sleep(2)

UIDinput = driver.find_element(By.XPATH, "//input[@name='userId']")
UIDinput.send_keys('015320')
time.sleep(1)
UIDinput.send_keys(Keys.ENTER)
time.sleep(1)
# button = driver.find_element_by_class_name('arrow')
# button.click()

PWDinput = driver.find_element(By.XPATH, "//input[@name='passwd']")
PWDinput.send_keys('!9880707apollo')
time.sleep(1)
PWDinput.send_keys(Keys.ENTER)
time.sleep(1)
try:
    but = driver.find_element_by_id('mini-21')
    but.send_keys(Keys.ENTER)
except:
    pass

time.sleep(1)

listitem = driver.find_element(By.XPATH, "//li[@name='M000002']")

listitem.click()
time.sleep(1)

driver.switch_to.frame('mini-iframe-17')
aitems = []
aitems = driver.find_elements(By.XPATH, "//div[@class='product clearfix']")

for aitem in aitems:

    if '外汇即期' in aitem.get_attribute("onclick") and 'cfetsfx' in aitem.get_attribute("onclick"):
        aitem.click()
    else:

        pass
time.sleep(1)
# print(driver.page_source)
driver.switch_to.default_content()
driver.switch_to.frame('mini-iframe-18')


selecta = driver.find_element(By.XPATH, "//td[@id='mini-48$headerCell2$1']")
print(selecta)



chanpininput = driver.find_element(By.XPATH, "//span[@id='approveStatus']")
chanpininput.click()
time.sleep(1)
zhuangtaiinput = driver.find_element(By.XPATH, "//tr[@id='mini-10$0']")
zhuangtaiinput.click()
time.sleep(1)

pager_size = driver.find_element(By.XPATH, "//span[@id='mini-51']")
pager_size.click()
time.sleep(1)
pageinput = driver.find_element(By.XPATH, "//tr[@id='mini-53$3']")
pageinput.click()
time.sleep(1)

search_btn = driver.find_element(By.XPATH, "//a[@id='search_btn']")
search_btn.click()


selectb = driver.find_element(By.XPATH, "//td[@id='mini-48$headerCell2$1']")
print(selectb)
print(selectb.get_attribute("class"))


selectbox = driver.find_element(By.XPATH, "//span[@id='mini-48checkall']")
print(selectbox)

selectbox.click()
time.sleep(1)

time.sleep(1)

# driver.close()
