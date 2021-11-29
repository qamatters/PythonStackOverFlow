from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.bet365.com/#/AC/B9/C20511432/D1/E148/F2/")

fightInfo = driver.find_element(By.CLASS_NAME, "sgl-MarketFixtureDetailsLabel")
americanOdds = driver.find_elements(By.CLASS_NAME, "sgl-MarketOddsExpand")

sleep(60)

driver.quit()