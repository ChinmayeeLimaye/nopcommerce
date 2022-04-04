import pytest
from PageObjects.LoginPage import Login
from utilities.customlogger import LogGeneration
from utilities.readconfig import ReadConfig
from utilities import XLutil
import time

class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = "/home/chinmayee/PycharmProjects/nopcommerce/TestData/LoginData.xlsx"
    logger = LogGeneration.loggen()  # Logger

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = XLutil.getRowCount(self.path, 'Sheet1')
        print('Number of rows...',self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLutil.readData(self.path,'Sheet1',r,1)
            self.password = XLutil.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLutil.readData(self.path, 'Sheet1', r, 3)

            self.lp.SetEmail(self.user)
            self.lp.SetPwd(self.password)
            self.lp.ClickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("**** passed ****")
                    self.lp.ClickLogout();
                    lst_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.info("**** failed ****")
                    self.lp.ClickLogout();
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            #print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");