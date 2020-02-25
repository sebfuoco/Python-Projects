import time
import win32api
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import winsound

duration = 5000  # milliseconds
freq = 1000  # Hz
args = ["hide_console", ] # optional, hides webdriver console
driver = webdriver.Chrome(service_args=args) # optional, hides webdriver console
driver.get("www.loginpage.com") # fetch login page
email = driver.find_element_by_name("email")
password = driver.find_element_by_name("password")

email.send_keys("example@email.com")
password.send_keys("passwordexample")
password.send_keys(Keys.ENTER)
time.sleep(1)
driver.get("www.webpage.com") # fetch webpage after login
while True:
    time.sleep(3)
    try:
        studies = driver.find_element_by_xpath('xpath').text
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue
    except NoSuchElementException:
        winsound.Beep(freq, duration)
        win32api.MessageBox(0, 'Something Happened!', 'ATTENTION')
        break
driver.quit()
