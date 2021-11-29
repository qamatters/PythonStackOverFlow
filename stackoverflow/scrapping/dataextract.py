from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://kbp.aero/en/")
driver.maximize_window()
sleep(3)
print(driver.find_element(By.CSS_SELECTOR, "div.table_wrp.out.today > table").text)
driver.quit()