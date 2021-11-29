from time import sleep
from selenium import webdriver

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("start-maximized")
option.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(PATH, options=option)
url = 'https://trade.mql5.com/trade'

driver.get(url)
driver.maximize_window()
sleep(40)

driver.quit()