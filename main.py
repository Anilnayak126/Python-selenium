from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(5)

driver.close()