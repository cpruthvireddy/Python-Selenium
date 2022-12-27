from selenium.webdriver.common.by import By


class Search:

    btnsearch = (By.XPATH, "//*[@id = 'search_btn']")

    def __init__(self,d):
        self.d = d

    def searchbtn(self):
        return self.d.find_element(*Search.btnsearch)
        # self.d.find_element(By.XPATH, "//*[@id = 'search_btn']").click()