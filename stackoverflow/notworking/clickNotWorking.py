from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"

option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("start-maximized")
option.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(PATH, options=option)

driver.get("https://shop.wegmans.com/login")
driver.maximize_window()
wait = WebDriverWait(driver, 20)
wait.until(EC.title_contains('Sign in'))

print("Page displayed successfully ")

driver.find_element(By.ID, "signInName").send_keys("myemail@yahoo.com")
driver.find_element(By.ID, "password").send_keys("password")
nextElement = driver.find_element(By.XPATH, '//*[@id="next"]')
print(nextElement.text)
nextElement.click()
sleep(10)
validationError = driver.find_element(By.XPATH, '//*[@class="error pageLevel"]//p').text
print(validationError)
driver.quit()
