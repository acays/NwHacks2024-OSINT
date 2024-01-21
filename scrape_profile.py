from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

import re
from selenium.common.exceptions import NoSuchElementException
# https://realpython.com/python-send-email/
def scrape_profile(driver, profile_urls) :
    for profile_url in profile_urls :
        driver.get(profile_url)
        wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
        # Get the title of the webpage
        current_url = driver.current_url


        # Check if "404" is in the title
        if "404" in current_url :
            continue
        else :
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Contact info']")))
            element.click()
            
            email, phone, website = find_contact_info(driver)
            print("email is ", email)
            print("phone is ", phone)
            print("website is ", website)

        # Close the Selenium WebDriver when you're done with it
    driver.quit()
def find_contact_info(driver) :
    html_content = driver.page_source

    phone_pattern = r'(?!(1253339631))\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    email_pattern = r'\b[A-Za-z0-9._%+-]+@(?!.*(?:png|jpg)\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

    website_pattern = r'https?://(?!(?:.*(?:static|linkedin|svg|w3|image))).*'

    is_phone = re.search(is_phone, html_content) is not None
    is_email = re.search(is_email, html_content) is not None
    is_website = re.search(is_website, html_content) is not None

    email_match = re.search(email_pattern, html_content)
    
    if email_match != None :
        email = email_match.group(0)
    
    website_match = re.search(website_pattern, html_content)
    
    if website_match != None :
        website = website_match.group(0)   
         
    phone_match = re.search(phone_pattern, html_content)
    
    if phone_match != None :
        phone = phone_match.group(0)


        
    return email, phone, website
    


   
            
