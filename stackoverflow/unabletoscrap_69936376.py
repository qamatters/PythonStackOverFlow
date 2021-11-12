from selenium.webdriver.support import expected_conditions as EC
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = 'https://solanabeach.io/validators'

driver.get(url)
driver.maximize_window()
WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-bordered maintable "
                                                "table-striped-even']//tbody/tr")))

columnHeader = driver.find_element(By.XPATH, "//table[@class='table table-bordered maintable "
                                             "table-striped-even']//thead")
print("---------------------------------------------------------------------------------------")
print(re.sub(r"\s+", '|', columnHeader.text.strip()))
print("---------------------------------------------------------------------------------------")
textInPage = driver.find_elements(By.XPATH, "//table[@class='table table-bordered maintable "
                                            "table-striped-even']//tbody/tr")
del textInPage[:2]
for element in textInPage:
    print(element.text)
    print("---------------------------------------------------------------------------------------")

driver.quit()
