from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    input_email_id="Email"
    input_password_id="Password"
    button_login_xpath="//button[@class='button-1 login-button']"
    button_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver
    def SetEmail(self,username):
        self.driver.find_element(By.ID, self.input_email_id).clear()
        self.driver.find_element(By.ID,self.input_email_id).send_keys(username)

    def SetPwd(self, passsword):
        self.driver.find_element(By.ID, self.input_password_id).clear()
        self.driver.find_element(By.ID, self.input_password_id).send_keys(passsword)

    def ClickLogin(self):
            self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def ClickLogout(self):
            self.driver.find_element(By.LINK_TEXT, self.button_logout_linktext).click()



