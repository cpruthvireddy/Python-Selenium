from selenium.webdriver.common.by import By


class Dest:

    tocity = (By.XPATH, "//*[@id = 'dest']")
    endcity = (By.XPATH, "//ul/li[@class = 'sub-city']")

    def __init__(self, d):
        self.d = d

    def destsel(self):
        return self.d.find_element(*Dest.tocity)
        # self.d.find_element(By.XPATH, "//*[@id = 'dest']").send_keys('Hyd')

    def searchend(self):
        return self.d.find_elements(*Dest.endcity)
        # destination = self.d.find_elements(By.XPATH, "//ul/li[@class = 'sub-city']")