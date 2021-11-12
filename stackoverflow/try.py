from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)
url1 = "https://soundcloud.com/mohanadsalem/adham-nabulsi-han-alan"
driver.get(url1)
cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
cookies.click()

track_info = []
try:
    genre = driver.find_element(By.CSS_SELECTOR, ".fullHero__info > a > span").text
    print(genre)
    track_info.append(genre)
except:
    track_info.append("None")

statics = driver.find_element(By.CSS_SELECTOR,".listenEngagement__footer > ul")
try:
    playbacks_count = statics.find_element(By.CSS_SELECTOR,"li[title*='play']").get_attribute("title").split()[0]
    track_info.append(playbacks_count)
except:
    track_info.append("None")

try:
    likes_count = statics.find_element(By.CSS_SELECTOR,"li[title*='like']").get_attribute("title").split()[0]
    track_info.append(likes_count)
except:
    track_info.append("None")

try:
    reposts_count = statics.find_element(By.CSS_SELECTOR,"li[title*='repost']").get_attribute("title").split()[0]
    track_info.append(reposts_count)
except:
    track_info.append("None")

    print(track_info)

driver.quit()