from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

testData = "TestUser@" + str(datetime.datetime.now())

driver.get('https://buggy.justtestit.org/register')
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(testData)
driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys(testData)
driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys(testData)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(testData)
driver.find_element(By.XPATH, '//*[@id="confirmPassword"]').send_keys(testData)
driver.find_element(By.XPATH, '//button[contains(.,"Register")]').click()

print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(.,'
                                                                                  '"Register")]//following'
                                                                                  '::div[contains(@class,'
                                                                                  '"alert")]'))).text)

driver.quit()
