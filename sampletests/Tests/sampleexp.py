from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

d = webdriver.Chrome(ChromeDriverManager().install())
d.get("https://www.redbus.in/")
d.implicitly_wait(10)
d.maximize_window()
d.find_element(By.XPATH, "//*[@id = 'src']").send_keys('Pul')
source = d.find_elements(By.XPATH, "//ul[@class = 'autoFill homeSearch']")
for start in source:
    # print(start.text)
    if start == 'Pulivendula':
        start.send_keys(Keys.ENTER)

d.find_element(By.XPATH, "//*[@id = 'dest']").send_keys('Hyd')
# destination = d.find_elements(By.XPATH, "//ul[@class = 'autoFill homeSearch']")
destination = d.find_elements(By.XPATH, "//ul/li[@class = 'sub-city']")
for end in destination:
    # print(end.text)
    if end == 'Ecil, Hyderabad':
        end.send_keys(Keys.ENTER)

d.find_element(By.XPATH, "//*[@id = 'onward_cal']").click()
d.find_element(By.XPATH, "//td[normalize-space()='31']").click()
d.find_element(By.XPATH, "//*[@id = 'search_btn']").click()
time.sleep(10)

