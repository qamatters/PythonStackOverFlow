from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = 'https://www.kucoin.com/news/categories/listing/'

driver.get(url)
driver.maximize_window()
sleep(5)

textInPage = driver.find_elements(By.XPATH, "//*[@class='mainTitle___mbpq1']/a")
date = driver.find_elements(By.XPATH, "//*[@class='mainTitle___mbpq1']/p")

for element in textInPage:
    print(re.findall(r'\(.*?\)', element.text))

for element in date:
    print(element.text)
