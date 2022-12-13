from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import bs4
import getpass
from selenium.common import exceptions
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
driver.get("https://m.facebook.com")
driver.maximize_window()
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
username.clear()
username.send_keys("01963**")
password.clear()
password.send_keys("*****")
# password=getpass.getpass()
time.sleep(10)
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='login']"))).click()
time.sleep(5)
driver.get("https://m.facebook.com/banglalinkdigital/?tsid=0.8277416894125471&source=result")
time.sleep(8)
check_height = driver.execute_script("return document.body.scrollHeight;") 
while True:
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          time.sleep(1)
          height = driver.execute_script("return document.body.scrollHeight;") 
          if height == check_height: 
                break 
          check_height = height
time.sleep(10)
comment=driver.find_element(By.XPATH,"//div[@id='feedback_inline_pfbid02adSwjA9wwgCqzKzoJcBjCLreRdqtmjGAkcYxmBpauFkPLpksfSeJCekgyFL8J6nml']//a[@class='_15kq _77li'][normalize-space()='Comment']").click()
time.sleep(5)
all_comments=driver.find_elements(By.XPATH,"//div[@class='_2b04']")
for f in all_comments:
    comment=f.find_element(By.CSS_SELECTOR,"div[data-commentid]").text
    print(comment)
    time.sleep(5)

