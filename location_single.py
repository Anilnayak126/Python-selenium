"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.delete_all_cookies()
query = 'laptop'
driver.get(f"https://www.amazon.com/s?k=laptop&crid=19SLQ53REWTEU&sprefix=laptop%2Caps%2C454&ref=nb_sb_noss_1")

#elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
#print(len(elems))
# for elem in elems:
#     print(elem.text)

time.sleep(5)


driver.close()

"""




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time

# Headless mode (optional)
options = Options()
#options.add_argument('--headless')

driver = webdriver.Edge(options=options)

# Set a higher page load timeout
driver.set_page_load_timeout(30)

# Retry mechanism to handle occasional failures
max_attempts = 3
query = 'laptop'

for attempt in range(max_attempts):
    try:
        driver.get(f"https://www.amazon.com/s?k={query}")
        
        # Use explicit wait
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "puis-card-container"))
        )

        # Process elements here
        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        print(len(elems))
        for elem in elems:
            print(elem.text)
        
        break  # If successful, exit the loop
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        time.sleep(5)  # Wait before retrying

# Properly close the browser
driver.quit()
