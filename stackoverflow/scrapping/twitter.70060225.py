from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import datetime
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

stock = 'TSLA'
# Get today
now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d')

# Get yesterday
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')

# Get tomorrow
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow = tomorrow.strftime('%Y-%m-%d')

URL = f"https://twitter.com/search?q={stock}%20lang%3Aen%20until%3A{tomorrow}%20since%3A{yesterday}%20-filter%3Alinks%20-filter%3Areplies&src=typed_query&f=live"
driver.get(URL)
driver.maximize_window()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@data-testid='tweet']")))


def get_tweet():
    tweets = driver.find_elements(By.XPATH, "//*[@data-testid='tweet']")
    for count, item in enumerate(tweets, start=1):
        print(str(count) + ": Tweet from twitter page")
        print("----------------------------------------------------------")
        print(item.text)
        print("----------------------------------------------------------")


get_tweet()

print("First page Tweet from twitter page")
action = ActionChains(driver)
action.key_down(Keys.ARROW_DOWN).perform()

driver.quit()
