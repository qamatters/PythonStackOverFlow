from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('file:///C:/Users/deepak.mathpal/Documents/DemoForAutoamtion/AutomationForm.html')
driver.maximize_window()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='loader' and contains(@style, 'none')]")))
driver.execute_script("document.querySelector('button[name=\"tryit\"]').click()")
demoText = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#demo")))
print(driver.execute_script("return document.querySelector('#demo').innerText"))
sleep(2)
driver.quit()