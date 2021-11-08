# 本地Chrome浏览器设置方法

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


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
        time.sleep(2)
        # button = driver.find_element_by_class_name('arrow')
        # button.click()

        PWDinput = self.driver.find_element(By.XPATH, "//input[@name='passwd']")
        PWDinput.send_keys(User.UserPassword)
        PWDinput.send_keys(Keys.ENTER)
        time.sleep(2)

        try:
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-21']")
            button.send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(2)
        return True

    def AutoSubmit(self, User):
        ItemList = self.driver.find_element(By.XPATH, "//li[@name='M000002']")
        ItemList.click()
        time.sleep(2)

        self.driver.switch_to.frame('mini-iframe-17')

        Products = self.driver.find_elements(By.XPATH, "//div[@class='product clearfix']")

        SubmitStatus = False

        for Product in Products:
            ProductName = Product.get_attribute("onclick")
            if User.PickProduct == 'SPOT' and '外汇即期' in ProductName and 'cfetsfx' in ProductName:
                Product.click()
                time.sleep(1)
                SubmitStatus = self.AutoSubmit_SPOT(User)
                break
            elif User.PickProduct == 'FWD' and '外汇远期' in ProductName and 'cfetsfx' in ProductName:
                Product.click()
                time.sleep(1)
                SubmitStatus = self.AutoSubmit_FWD(User)
                break
            elif User.PickProduct == 'SWAP' and '外汇掉期' in ProductName and 'cfetsfx' in ProductName:
                Product.click()
                time.sleep(1)
                SubmitStatus = self.AutoSubmit_SWAP(User)
                break

        return SubmitStatus

    def AutoSubmit_SPOT(self, User):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mini-iframe-18')

        # select "新建"
        approveStatus = self.driver.find_element(By.XPATH, "//span[@id='approveStatus']")
        approveStatus.click()
        time.sleep(2)
        approveStatus_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-10$0']")
        approveStatus_option.click()
        time.sleep(2)

        # select "Page_100"
        page_size = self.driver.find_element(By.XPATH, "//span[@id='mini-51']")
        page_size.click()
        time.sleep(2)
        page_size_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-53$3']")
        page_size_option.click()

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
            infobox = self.driver.find_element(By.XPATH, "//td[@id='mini-167$content']")
            print(infobox.text)
            button = self.driver.find_element(By.XPATH, "//a[@id='mini-168']")
            button.send_keys(Keys.ENTER)
        except:
            pass

        return True

    def AutoSubmit_FWD(self, User):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mini-iframe-18')

        # select "新建"
        approveStatus = self.driver.find_element(By.XPATH, "//span[@id='approveStatus']")
        approveStatus.click()
        time.sleep(2)
        approveStatus_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-11$0']")
        approveStatus_option.click()
        time.sleep(2)

        # select "Page_100"
        page_size = self.driver.find_element(By.XPATH, "//span[@id='mini-52']")
        page_size.click()
        time.sleep(2)
        page_size_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-54$3']")
        page_size_option.click()

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

    def AutoSubmit_SWAP(self, User):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mini-iframe-18')

        # select "新建"
        approveStatus = self.driver.find_element(By.XPATH, "//span[@id='approveStatus']")
        approveStatus.click()
        time.sleep(2)
        approveStatus_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-10$0']")
        approveStatus_option.click()
        time.sleep(2)

        # select "Page_100"
        page_size = self.driver.find_element(By.XPATH, "//span[@id='mini-51']")
        page_size.click()
        time.sleep(2)
        page_size_option = self.driver.find_element(By.XPATH, "//tr[@id='mini-53$3']")
        page_size_option.click()

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
