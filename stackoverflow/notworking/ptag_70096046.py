import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

wait = WebDriverWait(driver, 30)

driver.get("https://www.counselingcalifornia.com/Find-a-Therapist")

wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[id$='IFrame_htmIFrame']")))
select = Select(wait.until(EC.visibility_of_element_located((By.ID, "language_field"))))
select.select_by_value('ENG')

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#searchBtn"))).click()
time.sleep(20)
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//div[@id='searchResults']//div[@class='panel-body']//div[contains(@class,'card')]")))
time.sleep(2)
dunk = driver.find_elements(By.XPATH,
                            "//div[@id='searchResults']//div[@class='panel-body']//div[contains(@class,'card')]")
for dun in dunk:
    print("-------------------------------")
    phone = dun.find_element(By.XPATH, "//p[@id='phoneDiv_80863']").text
    print(phone)
