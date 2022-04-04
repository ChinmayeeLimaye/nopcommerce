from selenium.webdriver.common.by import By


class SearchPage:
    input_search_email="//input[@id='SearchEmail']"
    input_search_firstname="//input[@id='SearchFirstName']"
    input_search_lastname="//input[@id='SearchLastName']"
    button_search="//button[@id='search-customers']"
    table_xpath="// table[ @ id = 'customers-grid']"
    table_rows="// table[ @ id = 'customers-grid']//tbody/tr"
    table_column="// table[ @ id = 'customers-grid']//tbody/tr/td"


    def __init__(self,driver):
        self.driver= driver

    def setsearchemail(self,email):
        self.driver.find_element(By.XPATH, self.input_search_email).send_keys(email)

    def setsearchfirstname(self,fname):
        self.driver.find_element(By.XPATH, self.input_search_firstname).send_keys(fname)

    def setsearchlastname(self,lname):
        self.driver.find_element(By.XPATH, self.input_search_lastname).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element(By.XPATH, self.button_search).click()

    def getrows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_rows))

    def getcolumn(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column))

    def verifyemail(self,email):
        flag=False
        for r in range(1,self.getrows()+1):
            email_id=self.driver.find_element(By.XPATH,"// table[ @ id = 'customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            print(email_id)
            if email==email_id:
                flag=True
                break
        return flag


    def verifyname(self,fname):
        flag=False
        for r in range(1,self.getrows()+1):
            fnameid=self.driver.find_elements(By.XPATH,"// table[ @ id = 'customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if fname==fnameid:
                flag=True
                break
        return flag









