from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://bestdubbedanime.com/Demon-Slayer-Kimetsu-no-Yaiba/26")
WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,  "//div[@class='playostki']//img"))).click()
print(WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#my_video_1_html5_api > source"))).get_attribute("src"))
driver.quit()