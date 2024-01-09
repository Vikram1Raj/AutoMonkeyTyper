import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import keyboard as kb

#Initialize the Webdriver
url = "https://monkeytype.com/"
driver = webdriver.Firefox()
driver.get(url)

#Accepting Cookies
try:
  cookie_button = driver.find_element(By.CSS_SELECTOR,".active.acceptAll")
  accept_cookies = ActionChains(driver).click(cookie_button).perform()

except:
  print("Failed")

test_times = driver.find_elements(By.CSS_SELECTOR,".textButton.active")
actual_time = test_times[1].text

#Main Code
while True:

  words = driver.find_elements(By.CLASS_NAME,"word.active")

  for word in words:
    temp = word.text
    for string in temp:
      for char in string:
        kb.press_and_release(char)
        time.sleep(0.05)
        print(char)      
    kb.press_and_release("space")
    time.sleep(0.1)
  
  try:
    chart = driver.find_element(By.ID,"wpmChart")
    chart_height = chart.get_attribute("height")
    
    if chart_height == "200":
      break
  except:
    continue
  
acc_and_wpm = driver.find_elements(By.CLASS_NAME,"bottom")
print("ACC and WPM")

print(f"Time = {actual_time} secs ")
print(f"WPM = {acc_and_wpm[0].text}")
print(f"Acc = {acc_and_wpm[1].text}")

driver.quit()
    
 
    
    



