from telnetlib import EC
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = 'https://forms.nh.gov/licenseverification/'

driver.get(url)
driver.maximize_window()
sleep(5)

select_prof = driver.find_element(By.ID, 't_web_lookup__profession_name')
Select(select_prof).select_by_value('Dental')

select_lic_type = driver.find_element(By.ID, "t_web_lookup__license_type_name")
# select profession criteria value
Select(select_lic_type).select_by_value('Dentist')
sleep(1)

send = driver.find_element(By.ID, "t_web_lookup__last_name")
send.send_keys('A*')
sleep(1)
# click on check box
driver.switch_to.frame(0)
captcha = driver.find_element(By.CSS_SELECTOR, '.recaptcha-checkbox-border')
captcha.click()
# click search button
driver.find_element(By.XPATH, "sch_button").click()
sleep(1)
