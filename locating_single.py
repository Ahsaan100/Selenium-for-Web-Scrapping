from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.com/s?k={query}&crid=F595FCTFWC23&sprefix=lap%2Caps%2C1690&ref=nb_sb_noss_2")

elems = driver.find_elements(By.CLASS_NAME, "puis-card-container ")
print(f"{len(elems)} Items found")
for elem in elems:
    print(elem.text)


time.sleep(5)
driver.close()
