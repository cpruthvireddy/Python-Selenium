from selenium.webdriver.common.by import By


class Jrndate:

    journeydate = (By.XPATH, "//*[@id = 'onward_cal']")
    selectdate = (By.XPATH, "//td[normalize-space()='31']")

    def __init__(self, d):
        self.d = d

    def godate(self):
        return self.d.find_element(*Jrndate.journeydate)
        # self.d.find_element(By.XPATH, "//*[@id = 'onward_cal']").click()

    def seldate(self):
        return self.d.find_element(*Jrndate.selectdate)
        # self.d.find_element(By.XPATH, "//td[normalize-space()='31']").click()
