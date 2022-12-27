from selenium.webdriver.common.by import By


class SRC:

    frmcity = (By.XPATH, "//*[@id = 'src']")
    searchfrmcity = (By.XPATH, "//ul[@class = 'autoFill homeSearch']")

    def __init__(self, d):
        self.d = d

    def sourcesel(self):
        return self.d.find_element(*SRC.frmcity)
        # self.d.find_element(By.XPATH, "//*[@id = 'src']").send_keys('Pul')

    def searchsource(self):
        return self.d.find_elements(*SRC.searchfrmcity)
        # source = self.d.find_elements(By.XPATH, "//ul[@class = 'autoFill homeSearch']")


