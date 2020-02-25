import time
import win32api
import winsound
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

duration = 3000  # milliseconds
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
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div'))
        ) # report a TimeoutException if element does not exist for 10 seconds
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue
    except TimeoutException:
        winsound.Beep(freq, duration)
        win32api.MessageBox(0, 'New study at Prolific!', 'ATTENTION')
        break
driver.quit()
