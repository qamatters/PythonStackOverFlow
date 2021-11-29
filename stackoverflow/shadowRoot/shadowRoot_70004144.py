
from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def getShadowRoot(host):
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", host)
    return shadow_root

driver.get(
    'https://signon.service-now.com/ssologin.do?RelayState=%252Fapp%252Fservicenow_ud%252Fexks6phcbx6R8qjln0x7'
    '%252Fsso%252Fsaml%253FRelayState%253Dhttps%25253A%25252F%25252Fdeveloper.servicenow.com%25252Fdev.do&redirectUri'
    '=&email=')
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.find_element(By.NAME, 'username').send_keys('testqamatters@gmail.com')
wait.until(EC.element_to_be_clickable((By.ID, 'usernameSubmitButton'))).click()
# driver.find_element(By.ID, 'usernameSubmitButton').click()
# sleep(3)
wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys('Ranikhet@88')
# driver.find_element(By.NAME, 'password').send_keys('Ranikhet@88')
# sleep(3)

wait.until(EC.element_to_be_clickable((By.ID, 'submitButton'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value=’Submit’]"))).click()

# driver.find_element(By.ID, 'submitButton').click()
sleep(10)
print(driver.title)
sleep(3)
shadowDomHostElement0 = driver.find_element(By.CSS_SELECTOR, "dps-app[now-id]")
last0 = driver.execute_script("return arguments[0].shadowRoot", shadowDomHostElement0)
sleep(3)
shadowDomHostElement1 = last0.find_element(By.CSS_SELECTOR, "div > main > dps-home-auth-quebec")
last1 = driver.execute_script("return arguments[0].shadowRoot", shadowDomHostElement1)
sleep(3)
startButtonElement = last1.find_element(By.CSS_SELECTOR, "div > section:nth-child(1) > div > dps-page-header > div:nth-child(1) > button > span")
print(startButtonElement.text)

startButtonElement.click()
sleep(5)

driver.quit()

