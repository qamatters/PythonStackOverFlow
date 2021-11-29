from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.mobil.com/en/lubricants/what-to-buy/find-the-right-motor-oil/")
driver.maximize_window();
driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
driver.implicitly_wait()
driver.find_element(By.XPATH, "(//div[@class='select-wrapper noTriggerAnalyticsEvent right-arrow-select'])[1]").send_keys(Keys.ENTER)
