from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.common.exceptions import NoSuchElementException
def scrape_profile(driver, profile_urls) :
    for profile_url in profile_urls :
        print(profile_url)
    
        
        # try:
        #     driver.get(profile_url)
        #     wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
        #     element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Contact info']")))
        #     element.click()
        

        # except NoSuchElementException:
        #     # Handle the case where the element is not found
        #     print("Profile", profile_url, " was not found (404)")
        driver.get(profile_url)
        wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
        # Get the title of the webpage
        current_url = driver.current_url
        print("url is", current_url)

        # Check if "404" is in the title
        if "404" in current_url :
            continue
        else :
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Contact info']")))
            element.click()

        # Close the Selenium WebDriver when you're done with it
    driver.quit()
        
