from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import random

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.vivanuncios.com.mx/')
driver.maximize_window()

price_input = driver.find_element(By.XPATH, "//input[@class='filter-text']")
price_input.send_keys("1,500,000")

select_input = driver.find_element(By.XPATH,
                                   "/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/section[1]/div[1]/section[1]/div["
                                   "1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
select_input.click()

casa_input = driver.find_element(By.XPATH, "//li[@data-value='/s-casas-en-venta/v1c1293p1']")
casa_input.click()

location_input = driver.find_element(By.XPATH, "//span[@class='location-text']")
location_input.click()

box_location_input = driver.find_element(By.XPATH, "//input[@id='locationPicker-input']")
box_location_input.send_keys("Querétaro, México")
sleep(random.uniform(8.0, 10.0))

select_location = driver.find_element(By.XPATH,
                                      "//li[1]//span[@class='description']//b[contains(text(),'Querétaro, México')]")
select_location.click()

location_btn = driver.find_element(By.XPATH, "//span[@class='sudolink']")
location_btn.click()

search_btn = driver.find_element(By.XPATH, "//div[@class='location-input-btn']")
search_btn.click()

sleep(60)

driver.quit()
