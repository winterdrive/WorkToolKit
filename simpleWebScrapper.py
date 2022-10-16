import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


PATH="C:/Users/XXX/OneDrive/桌面/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://www.flickr.com/photos/*************")


for i in range(0,1000):
    time.sleep(1)
    downloadIcon=driver.find_element(By.CLASS_NAME, "ui-icon-download")
    downloadIcon.click()
    time.sleep(1)
    downloadIconOri=driver.find_element(By.CLASS_NAME, "原本大小")
    downloadIconOri.click()
    time.sleep(1)
    otherClick=driver.find_element(By.CSS_SELECTOR,".fluid-modal-overlay")
    otherClick.click()
    time.sleep(1)
    nextPageSpan=driver.find_element(By.CSS_SELECTOR,".slider>.nextImages")
    print(nextPageSpan)
    nextPageSpan.click()
