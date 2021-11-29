from time import sleep
from selenium import webdriver
import pandas as pd
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://opensea.io/rankings')
sleep(3)
driver.maximize_window()

other_services = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[2]/div')
print(other_services.text)

driver.quit()