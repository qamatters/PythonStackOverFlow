from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://selectorshub.com/xpath-practice-page')
driver.maximize_window()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"pact")))
element = driver.execute_script("return document.querySelector('#snacktime').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza')")
element.send_keys(Keys.TAB)
actions = ActionChains(driver)
actions.send_keys("I prefer tea")
actions.perform()
sleep(10)
driver.quit()

