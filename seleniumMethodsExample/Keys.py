from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = 'https://www.finewineandgoodspirits.com'

driver.get(url)
driver.maximize_window()
sleep(20)
yesButton = driver.find_element(By.XPATH, '//*[@id="ltkpopup-age-gate-yes"]')
yesButton.click()
closeButton = driver.find_element(By.CLASS_NAME, "ltkpopup-close")
closeButton.click()

driver.get("https://www.finewineandgoodspirits.com/webapp/wcs/stores/servlet/LogonForm?langId=-1&storeId=10051"
           "&catalogId=10051")

email = driver.find_element(By.NAME, "logonId")
email.send_keys("mccallister81@gmail.com")
driver.implicitly_wait(5)
password = driver.find_element(By.NAME, "logonPassword")
password.send_keys("Envision1")
sleep(10)
loginButton = driver.find_element(By.XPATH, "(//div[@title='Member Login']//following::a)[2]")
print(loginButton.get_attribute("title"))
loginButton.send_keys(Keys.ENTER)