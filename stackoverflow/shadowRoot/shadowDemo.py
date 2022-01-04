from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('file:///C:/Users/deepak.mathpal/Documents/shadowDom.html')
driver.maximize_window()
ageElement = driver.find_element(By.ID, 'age')
ageElement.send_keys(30)
ageElement.send_keys(Keys.TAB)
actions = ActionChains(driver)
actions.send_keys("Deepak")
actions.perform()
sleep(10)
driver.quit()