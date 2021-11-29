from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym=700&sc_lang=en/")
driver.maximize_window()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Export to Excel"))).click()