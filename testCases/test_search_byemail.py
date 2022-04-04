import time

from PageObjects.Add_customer import Add_customer
from PageObjects.LoginPage import Login
from PageObjects.SearchPage import SearchPage
from utilities.customlogger import LogGeneration
from utilities.readconfig import ReadConfig


class Test_004_SearchByEmail:
        baseURL = ReadConfig.getApplicationURL()
        username = ReadConfig.getUseremail()
        password = ReadConfig.getPassword()
        logger = LogGeneration.loggen()

        def test_searchemail(self,setup):
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.lp = Login(self.driver)
            self.lp.SetEmail(self.username)
            self.lp.SetPwd(self.password)
            self.lp.ClickLogin()

            self.ac = Add_customer(self.driver)
            self.ac.click_customer()
            time.sleep(3)
            self.ac.click_customer_submenu()


            self.se=SearchPage(self.driver)
            self.se.setsearchemail("brenda_lindgren@nopCommerce.com")
            self.se.clicksearch()

            time.sleep(5)

            status=self.se.verifyemail("brenda_lindgren@nopCommerce.com")
            assert True==status

