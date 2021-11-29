import time
from selenium.webdriver.common.by import By
from selenium import webdriver

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"

option = webdriver.ChromeOptions()

driver = webdriver.Chrome(PATH)

driver.get("https://myterminal.ect.nl/app/object-schedule")
time.sleep(10)

startButtonElement = driver.ExecuteScript("return document.querySelector('body > ect-cookie-dialog').shadowRoot.querySelector('#cookie-dialog').shadowRoot.querySelector('#cookie-dialog > div._ect-cookie-dialog__links > div > ect-button')")
startButtonElement.click()


time.sleep(3)
