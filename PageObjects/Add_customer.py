import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_customer:
    customer_menu="// a[ @ href = '#'] // p[contains(text(), 'Customers')]"
    customer_sub_menu="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_add_new="//a[normalize-space()='Add new']"
    input_email="//input[@id='Email']"
    input_password="//input[@id='Password']"
    input_first_name="//input[@id='FirstName']"
    input_last_name="//input[@id='LastName']"
    input_male_id="Gender_Male"
    input_female_id="Gender_Female"
    input_DOB="//input[@id='DateOfBirth']"
    input_company="//input[@id='Company']"
    input_tax_checkbox_id="IsTaxExempt"
    input_newsletteer="//div[@class='input-group-append']//div[@role='listbox']"
    input_registered="//li[contains(text(),'Registered')]"
    input_administrator="//li[contains(text(),'Administrators')]"
    input_guests="//li[contains(text(),'Guests')]"

    input_forum="//li[contains(text(),'Forum Moderators')]"
    select_manager="// select[ @ id = 'VendorId']"
    input_admin_comment="//textarea[@id='AdminComment']"
    save="//button[@name='save']"
    input_customer_roles="//div[@class='input-group-append input-group-required']//div[@role='listbox']"

    def __init__(self,driver):
        self.driver=driver

    def click_customer(self):
        self.driver.find_element(By.XPATH, self.customer_menu).click()

    def click_customer_submenu(self):
        self.driver.find_element(By.XPATH, self.customer_sub_menu).click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.button_add_new).click()

    def Set_Email(self,email):
        self.driver.find_element(By.XPATH,self.input_email).send_keys(email)

    def Set_pass(self,pwd):
        self.driver.find_element(By.XPATH,self.input_password).send_keys(pwd)

    def Set_Firstname(self,fname):
        self.driver.find_element(By.XPATH,self.input_first_name).send_keys(fname)


    def Set_Lastname(self,lname):
        self.driver.find_element(By.XPATH,self.input_last_name).send_keys(lname)


    def select_gender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.input_male_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID, self.input_female_id).click()
        else:
            self.driver.find_element(By.ID, self.input_male_id).click()

    def Set_DOB(self,dob):
        self.driver.find_element(By.XPATH,self.input_DOB).send_keys(dob)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.input_customer_roles).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.input_registered)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.input_administrator)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.input_guests)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.input_vendor)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.input_guests)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)


    def select_manager_drop(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.select_manager))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.input_admin_comment).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.save).click()

    def set_company(self,value):
        self.driver.find_element(By.XPATH,self.input_company).send_keys(value)