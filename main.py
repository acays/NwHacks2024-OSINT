from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
def login(driver) :
    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/uas/login")

    # Wait for the email input field to appear
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Enter your email address
    email_field.send_keys("jaxotaj353@rentaen.com")

    # Locate and enter the password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("h3TEP_r4r-8i-Un")

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for the LinkedIn home page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "global-nav"))
    )
    
    # For demonstration purposes, let's print the page title
    # print("Page title:", driver.title)

    # Enter a search query
    # search_bar.send_keys("Bill Gates")
    
def find_users_with_job(driver) :
     # At this point, you are logged in, and you can continue with your automated tasks

    # Locate the search bar by its class name
    search_bar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")

    

    # Simulate pressing Enter to perform the search
    search_bar.send_keys(Keys.RETURN)

    driver.get("https://www.google.com")

    # locate search form by_name
    search_query = driver.find_element(By.NAME, "q")

    # send_keys() to simulate the search text key strokes
    search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')
    search_query.send_keys(Keys.RETURN)
    # Wait for the search results to load (you may adjust the timeout)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
    
    results = driver.find_elements_by_css_selector('div.g')

    # urls = [result.get_attribute('href') for result in result_elements]
    
    
    print(results)
    # first_result = driver.find_element(By.CSS_SELECTOR, "h3")
    # first_result.click()

if __name__ == "__main__" :

    # Initialize the WebDriver (Chrome)
    driver = webdriver.Chrome()

    login(driver)

    find_users_with_job(driver)


    driver.quit()
