# 本地Chrome浏览器设置方法

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class WebDriverApproverContorl:
    WebURL = ''
    driver = ''

    def __init__(self):
        self.driver = webdriver.Chrome()

    def setURL(self, url):
        self.WebURL = url

    def logWEB(self, Approver):
        self.driver.maximize_window()
        self.driver.get(self.WebURL)
        time.sleep(2)

        UIDinput = self.driver.find_element(By.XPATH, "//input[@name='userId']")
        UIDinput.send_keys(Approver.UserName)
        UIDinput.send_keys(Keys.ENTER)
        time.sleep(2)
        # button = driver.find_element_by_class_name('arrow')
        # button.click()

        PWDinput = self.driver.find_element(By.XPATH, "//input[@name='passwd']")
        PWDinput.send_keys(Approver.UserPassword)
        PWDinput.send_keys(Keys.ENTER)
        time.sleep(2)

        try:
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-21']")
            button.send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(2)
        return True

    def AutoApprove(self, Approver):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mini-iframe-16')

        # select "正式交易"
        TypeList = self.driver.find_element(By.XPATH, "//input[@id='tradeType$text']")
        TypeList.click()
        time.sleep(2)
        Type_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-4$1']")
        Type_option.click()
        time.sleep(2)

        Approver.PickProduct = ["SPOT", "FWD", "SWAP"]

        for Product in Approver.PickProduct:
            if Product == 'SPOT':
                ApproveStatus = self.Approve_SPOT(Approver)
                break
            elif Product == 'FWD':
                ApproveStatus = self.Approve_FWD(Approver)
                break
            elif Product == 'SWAP':
                ApproveStatus = self.Approve_SWAP(Approver)
                break

        return ApproveStatus

    def Approve_SPOT(self, Approver):
        # select "外汇即期"
        ProductList = self.driver.find_element(By.XPATH, "//input[@id='prdName$text']")
        ProductList.click()
        time.sleep(2)
        Product_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-7$16']")
        Product_option.click()
        time.sleep(2)

        # click search_btn
        search_btn = self.driver.find_element(By.XPATH, "//a[@id='search_btn']")
        search_btn.click()
        time.sleep(4)

        # select "All Selected"
        checkbox = self.driver.find_element(By.XPATH, "//td[@id='mini-42$headerCell2$1']")
        checkbox.click()
        time.sleep(1)

        commit_btn = self.driver.find_element(By.XPATH, "//a[@id='batch_approve_btn']")
        commit_btn.click()

        time.sleep(2)

        try:
            infobox = self.driver.find_element(By.XPATH, "//td[@id='mini-167$content']")
            print(infobox.text)
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-168']")
            button.send_keys(Keys.ENTER)
        except:
            pass

        return True

    def Approve_FWD(self, Approver):
        # select "外汇远期"
        ProductList = self.driver.find_element(By.XPATH, "//input[@id='prdName$text']")
        ProductList.click()
        time.sleep(2)
        Product_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-7$16']")
        Product_option.click()
        time.sleep(2)

        # click search_btn
        time.sleep(2)
        search_btn = self.driver.find_element(By.XPATH, "//a[@id='search_btn']")
        search_btn.click()
        time.sleep(4)

        # select "All Selected"
        checkbox = self.driver.find_element(By.XPATH, "//td[@id='mini-49$headerCell2$1']")
        checkbox.click()
        time.sleep(1)

        commit_btn = self.driver.find_element(By.XPATH, "//a[@id='batch_commit_btn']")
        commit_btn.click()
        time.sleep(2)

        try:
            infobox = self.driver.find_element(By.XPATH, "//td[@id='mini-195$content']")
            print(infobox.text)
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-196']")
            button.click()
        except:
            pass

        return True

    def Approve_SWAP(self, Approver):
        # select "外汇掉期"
        ProductList = self.driver.find_element(By.XPATH, "//input[@id='prdName$text']")
        ProductList.click()
        time.sleep(2)
        Product_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-7$16']")
        Product_option.click()
        time.sleep(2)

        # click search_btn
        time.sleep(2)
        search_btn = self.driver.find_element(By.XPATH, "//a[@id='search_btn']")
        search_btn.click()
        time.sleep(4)

        # select "All Selected"
        checkbox = self.driver.find_element(By.XPATH, "//td[@id='mini-48$headerCell2$1']")
        checkbox.click()
        time.sleep(1)

        commit_btn = self.driver.find_element(By.XPATH, "//a[@id='batch_commit_btn']")
        commit_btn.click()

        time.sleep(2)

        try:
            infobox = self.driver.find_element(By.XPATH, "//td[@id='mini-161$content")
            print(infobox.text)
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-162']")
            button.click()
        except:
            pass

        return True

    def closeWEB(self, User):
        time.sleep(8)
        self.driver.close()

        return True
