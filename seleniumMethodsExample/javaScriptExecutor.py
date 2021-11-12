from time import sleep

from selenium import webdriver

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.album.alexflueras.ro/index.php')
driver.maximize_window()
sleep(3)

driver.execute_script("window.scrollBy(2000,0)")
sleep(5)

driver.quit()