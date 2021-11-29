import time

import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

page = 1
while page <= 10:
    driver.get(
        'https://forum.bouyguestelecom.fr/questions/browse?flow_state=published&order=created_at.desc&page=' + str(
            page) + '&utf8=✓&search=&with_category%5B%5D=2483')
    driver.maximize_window()
    print("Page  url: " + driver.current_url)
    time.sleep(1)

    if page == 1:
        AcceptButton = driver.find_element(By.ID, 'popin_tc_privacy_button_3')
        AcceptButton.click()

    questions = driver.find_elements(By.XPATH, '//div[@class="corpus"]//a[@class="content_permalink"]')

    for count, item in enumerate(questions, start=1):
        print(str(count) + ": question detail:")
        questionfount = driver.find_element(By.XPATH,
                                            "(//div[@class='corpus']//a[@class='content_permalink'])[" + str(
                                                count) + "]")
        questionfount.click()
        questionInPage = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(//p[@class='old-h1']//following::div[contains(@__uid__, "
                       "'dim')]//div[@class='corpus']//a["
                       "@class='content_permalink'])[1]")))
        author = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(//p[@class='old-h1']//following::div[contains(@__uid__, 'dim')]//div["
                       "@class='corpus']//div[contains(@class, 'metadata')]//dl["
                       "@class='author-name']//a)[1]")))
        date = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(//p[@class='old-h1']//following::div[contains(@__uid__, 'dim')]//div["
                       "@class='corpus']//div[contains(@class, 'metadata')]//dl[@class='date']//dd)[1]")))

        print(questionInPage.text)
        print(author.text)
        print(date.text)
        print(
            "-----------------------------------------------------------------------------------------------------------")
        driver.back()
        driver.refresh()
    page = page + 1

driver.quit()
