from selenium import webdriver
PATH = r"C:\\bin\\chromedriver.exe"
driver = webdriver.Chrome(PATH)    #here we are using the chrome web-driver for which the path is mentioned 

#now in order to open a web-page and also close it 

driver.get("https://en.wikipedia.org/wiki/Python_(programming_language")
#to get the title of the web-page we are accessing: 
print(driver.title)
driver.close()   #driver.close() closes the tab, driver.quit() quits the browser