from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #this will allow us to hit enter on the search bar element 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = r"C:\\bin\\chromedriver.exe"
driver = webdriver.Chrome(PATH)    #here we are using the chrome web-driver for which the path is mentioned 

#now in order to open a web-page and also close it 

driver.get("https://en.wikipedia.org/wiki/Python_(programming_language")
#to get the title of the web-page we are accessing: 
print(driver.title)
search = driver.find_element_by_id("searchInput")     #you can find element by id name class and so on 

search.clear()                                        #this is done to prevent any previous text from being appended
search.send_keys("computer")                          #this is the term we are inputting in the search bar 
search.send_keys(Keys.RETURN)                                    #hitting the enter/carriage return key


#to simply look at the page source
#print(driver.page_source)

#to avoid searching for the main element id before before the next page opens up
#To solve that, we will use an explicit wait that ensures that the id is searched in the next page and not the previous one

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mw-content-text"))
    )

    
    #print(main.text)  this prints all the text on the web page content area

    #to simply print the headers of the articles

    articles  = driver.find_elements_by_class_name("mw-search-result")

    #printing each article

    for article in articles:
        header = article.find_element_by_class_name("mw-search-result-heading")
        print(header.text)

finally:
    driver.close()






#to delay the close by 5 secs
time.sleep(5)

driver.close()   #driver.close() closes the tab, driver.quit() quits the browser