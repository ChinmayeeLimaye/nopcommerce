import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.LoginPage import Login
from utilities.customlogger import LogGeneration
from utilities.readconfig import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGeneration.loggen()

    @pytest.mark
    def test_login(self,setup):
        self.logger.info("Started 1st Test Case")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.SetEmail(self.username)
        self.lp.SetPwd(self.password)
        self.lp.ClickLogin()
        actual_title=self.driver.title
        assert "Dashboard / nopCommerce administration" in actual_title



