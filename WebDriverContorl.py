# 本地Chrome浏览器设置方法
import json

from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from UserDict import UserDict


class WebDriverContorl:
    WebURL = ''
    driver = ''

    def __init__(self):
        self.driver = webdriver.Chrome()

    def setURL(self, url):
        self.WebURL = url

    def logWEB(self, User):
        self.driver.maximize_window()
        self.driver.get(self.WebURL)
        time.sleep(2)

        UIDinput = self.driver.find_element(By.XPATH, "//input[@name='userId']")
        UIDinput.send_keys(User.UserName)
        UIDinput.send_keys(Keys.ENTER)
        time.sleep(1)
        # button = driver.find_element_by_class_name('arrow')
        # button.click()

        PWDinput = self.driver.find_element(By.XPATH, "//input[@name='passwd']")
        PWDinput.send_keys(User.UserPassword)
        PWDinput.send_keys(Keys.ENTER)
        time.sleep(1)

        try:
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-21']")
            button.send_keys(Keys.ENTER)
        except:
            pass
        return True

    def AutoSubmit(self, User):
        ItemList = self.driver.find_element(By.XPATH, "//li[@name='M000002']")
        ItemList.click()
        time.sleep(1)

        self.driver.switch_to.frame('mini-iframe-17')

        Products = self.driver.find_elements(By.XPATH, "//div[@class='product clearfix']")

        for Product in Products:
            if User.PickProduct == 'SPOT' and '外汇即期' in Product.get_attribute(
                    "onclick") and 'cfetsfx' in Product.get_attribute("onclick"):
                Product.click()
            elif User.PickProduct == 'FWD' and '外汇远期' in Product.get_attribute(
                    "onclick") and 'cfetsfx' in Product.get_attribute("onclick"):
                Product.click()
            elif User.PickProduct == 'SWAP' and '外汇掉期' in Product.get_attribute(
                    "onclick") and 'cfetsfx' in Product.get_attribute("onclick"):
                Product.click()
            else:
                pass

        time.sleep(1)
        # print(driver.page_source)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mini-iframe-18')

        # select "新建"
        approveStatus = self.driver.find_element(By.XPATH, "//span[@id='approveStatus']")
        approveStatus.click()
        time.sleep(1)
        try:
            approveStatus_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-10$0']")
        except:
            approveStatus_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-11$0']")
        approveStatus_option.click()
        time.sleep(1)

        # select "Page_100"
        try:  # SPOT & SWAP
            page_size = self.driver.find_element(By.XPATH, "//span[@id='mini-51']")
            page_size.click()
            time.sleep(1)
            page_size_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-53$3']")
            page_size_option.click()
        except:  # FWD
            page_size = self.driver.find_element(By.XPATH, "//span[@id='mini-52']")
            page_size.click()
            time.sleep(1)
            page_size_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-54$3']")
            page_size_option.click()

        time.sleep(1)
        search_btn = self.driver.find_element(By.XPATH, "//a[@id='search_btn']")
        search_btn.click()
        time.sleep(4)

        # select "All Selected"

        try:  # SPOT & SWAP
            checkbox = self.driver.find_element(By.XPATH, "//td[@id='mini-48$headerCell2$1']")
            checkbox.click()
        except:  # FWD
            checkbox = self.driver.find_element(By.XPATH, "//td[@id='mini-49$headerCell2$1']")
            checkbox.click()
            pass

        time.sleep(1)

        commit_btn = self.driver.find_element(By.XPATH, "//a[@id='batch_commit_btn']")
        commit_btn.click()

        time.sleep(1)

        try:
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-170']")
            button.send_keys(Keys.ENTER)
            print('请至少选择一条要提交的交易!')
        except:
            pass
        try:
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-196']")
            button.send_keys(Keys.ENTER)
            print('请至少选择一条要提交的交易!')
        except:
            pass
        try:
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-162']")
            button.send_keys(Keys.ENTER)
            print('请至少选择一条要提交的交易!')
        except:
            pass

        return True

    def closeWEB(self, User):
        time.sleep(10)
        self.driver.close()

        return True
