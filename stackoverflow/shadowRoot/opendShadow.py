from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('chrome://downloads/')
# driver.maximize_window()

# What if we use xpath or any other locator here
# searchDownloadFieldWithXpath = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
# searchDownloadFieldWithXpath.send_keys("Order_ID_2363900762.pdf")


# Using java script executor
searchDownload = driver.execute_script("return document.querySelector('body > downloads-manager').shadowRoot.querySelector('#toolbar').shadowRoot.querySelector('#toolbar').shadowRoot.querySelector('#search').shadowRoot.querySelector('#searchInput')")
searchDownload.send_keys("Order_ID_2363900762.pdf")
sleep(5)
print("Text is entered successfully")
sleep(10)
driver.quit()

