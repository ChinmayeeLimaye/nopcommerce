import random
import string
import time

from selenium.webdriver.common.by import By

from PageObjects.Add_customer import Add_customer
from PageObjects.LoginPage import Login
from utilities.customlogger import LogGeneration
from utilities.readconfig import ReadConfig


class Test_002_Add_cust:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGeneration.loggen()

    def test_add_customer(self, setup):
        self.logger.info("Started Add Customer Test Case")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.SetEmail(self.username)
        self.lp.SetPwd(self.password)
        self.lp.ClickLogin()
        self.ac=Add_customer(self.driver)
        self.ac.click_customer()
        time.sleep(3)
        self.ac.click_customer_submenu()
        self.ac.click_add_new()
        self.email=random_generator()+"@gmail.com"
        self.ac.Set_Email(self.email)
        self.ac.Set_pass("diplomat")
        self.ac.Set_Firstname("Chims")
        self.ac.Set_Lastname("Lims")
        self.ac.select_gender("Female")
        self.ac.Set_DOB("8/21/1990")
        self.ac.set_company("QA Activity")
        #time.sleep(3)
        self.ac.setCustomerRoles("Vendors")
        self.ac.select_manager_drop("Vendor 1")
        self.ac.setAdminContent("Hi this is new customer")
        self.ac.clickOnSave()

        self.success_msg=self.driver.find_element(By.TAG_NAME,"body").text

        #print(self.success_msg)

        if 'customer has been added successfully.' in self.success_msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot("/home/chinmayee/PycharmProjects/nopcommerce/Screenshots/Failed.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))