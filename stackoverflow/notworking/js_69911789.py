
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import random

PATH = r"C:\Users\deepak.mathpal\IdeaProjects\Selenium4\src\main\resources\chromedriver_chrome_95\chromedriver.exe"
driver = webdriver.Chrome(PATH)

js = '''var xhr = new XMLHttpRequest();
xhr.open('POST', 'http://httpbin.org/post', false);
xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

xhr.send('login=test&password=test');
return xhr.response;'''

result = driver.execute_script(js);

print(result)

driver.quit()