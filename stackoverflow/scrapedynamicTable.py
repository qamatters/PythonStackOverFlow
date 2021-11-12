import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.depositaccounts.com/banks/assets.aspx?instType=&stateType=hq&state=")
# print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "assetsTable"))).text)

tabelHeaderLocator = driver.find_element(By.CSS_SELECTOR, "#assetsTable > tbody > tr:nth-child(1)")

print(re.sub(r"\s+", '|', tabelHeaderLocator.text.strip()))

tableData = driver.find_elements(By.CSS_SELECTOR, "#assetsTable > tbody > tr")
del tableData[:1]

for element in tableData:
    print(element.text)

driver.quit()
