from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #this will allow us to hit enter on the search bar element 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r"C:\\bin\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

search = driver.find_element_by_id("searchInput")
search.clear()
search.send_keys("selenium", Keys.RETURN)


try:
    element1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Selenium (software)"))
    )

    element1.click()
    
    time.sleep(7)


    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mw-wiki-logo"))
    )
    element2.click()



    time.sleep(10)
finally:
    driver.quit()