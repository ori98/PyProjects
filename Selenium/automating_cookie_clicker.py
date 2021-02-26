#automating cookie clicker with selenium


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#actionchains perform a series of actions 

#adding implicit wait 

PATH = r"C:\\bin\\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

#creating a list of upgrades (buying grandmas first and then buying pointers)

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if (value <= count):
            #execute a new set of actions 
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
    