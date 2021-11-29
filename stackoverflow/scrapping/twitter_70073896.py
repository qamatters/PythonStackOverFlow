from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import datetime
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)
URL = "https://twitter.com/login"

driver.get(URL)
driver.maximize_window()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "text"))).send_keys("your username")
driver.find_element(By.XPATH, '(//*[@role="button"]//following::span[contains(.,"Next")])[2]').click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("your passowrd")
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='LoginForm_Login_Button']"))).click()
sleep(5)

imagePath = driver.find_element(By.XPATH, "//*[@data-testid='fileInput']")

imagePath.send_keys("C:\\Users\\username\\Documents\\Personal\\selenium.png")

tweetButton = driver.find_element(By.XPATH, "//*[@data-testid='tweetButtonInline']")

tweetButton.click()




