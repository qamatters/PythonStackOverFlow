from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = 'https://healthscreening.schools.nyc/?type=G'

driver.get(url)
driver.maximize_window()

sleep(5)

last_name = driver.find_element(By.XPATH, '//*[@id="guest_last_name"]')
last_name.send_keys('test test')
email = driver.find_element(By.XPATH, '//*[@id="guest_email"]')
email.send_keys('testtest@gmail.com')
button = driver.find_element(By.XPATH, '//*[@id="btnDailyScreeningSubmit"]/button')
button.click()

sleep(5)

driver.quit()