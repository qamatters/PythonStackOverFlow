from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver


PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.walmart.ca/rollback?f=12+51&icid=homepage_HP_TopCategory_Rollbacks_WM&sort=Popular%3ADESC&price=20-100')
sleep(3)
driver.maximize_window()

all_products = driver.find_element(By.XPATH, "*//div[@class='css-1gwszhe e1pmil1x10']")
print(all_products.text)

driver.quit()
