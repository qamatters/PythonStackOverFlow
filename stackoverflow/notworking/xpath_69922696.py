from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.scrapethissite.com/pages/")
driver.maximize_window()

sleep(5)

listOfKeywords = ['AJAX', 'Click']

for keyword in listOfKeywords:
    try:
        element = driver.find_element(By.XPATH, "//*[contains(text(),'{}')]".format(keyword))
        parent = element.find_element(By.XPATH, "./parent::*").get_attribute("class")
        tag_class = element.get_attribute("class")
        print(f"{keyword} : Parent tag class - {parent}, tag class-name - {tag_class}")
    except:
        print("Keyword not found")