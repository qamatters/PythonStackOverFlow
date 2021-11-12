from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url_first_part = "https://www.ebay.com/b/Apple/bn_21819543"

for i in range(5):
    i = i + 1
    url = url_first_part + "?_pgn=" + str(i)
    driver.get(url)
    sleep(3)
    driver.maximize_window()
    products = driver.find_element(By.XPATH, '//*[@id="s0-27-9-0-1[0]-0-1"]/ul')
    print(products.text)

driver.quit()
