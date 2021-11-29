from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.supremenewyork.com/shop/all")
link = driver.find_element(By.XPATH, '//*[@id="container"]/article[234]/div/a')
link.click()
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input"))).click()
element1 = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/a[2]"))).click()