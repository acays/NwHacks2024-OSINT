from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

import re
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import json
import os
# https://realpython.com/python-send-email/
def scrape_profile(driver, profile_urls, file_name) :
    if file_name != "secret_scrape.json" :
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
                
                email, phone = find_contact_info(driver)
                append_profile_to_json(file_name, profile_url, email, phone)
    
    else :
            
        driver.get("https://www.linkedin.com/in/test-tester-3538a82ab/overlay/contact-info/")

        find_contact_info(driver)
        email, phone = find_contact_info(driver)
        append_profile_to_json(file_name, "https://www.linkedin.com/in/test-tester-3538a82ab/overlay/contact-info/", email, phone)
    driver.quit()


def append_profile_to_json(file_name, link, email, phone):
    data = {}  # Create a dictionary to store the data

    # Check if the JSON file already exists
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)

    # Initialize the "profiles" key if it doesn't exist
    if "profiles" not in data:
        data["profiles"] = []

    # Create a profile dictionary
    profile = {
        "link": link,
        "email": email,
        "phone": phone
    }

    # Append the new profile to the "profiles" list
    data["profiles"].append(profile)

    # Write the updated data back to the JSON file
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage:
if __name__ == "__main__":
    file_name = "profiles.json"
    link = "https://example.com/link"
    email = "example@example.com"
    phone = "123-456-7890"
    append_profile_to_json(file_name, link, email, phone)

def find_contact_info(driver) :
    
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    # time.sleep(1000000)
    elements = WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[class*="link-without-visited-state"][class*="t-14"]'))
    )
      
    try:
        phone = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class="t-14 t-black t-normal"]'))
        ).text
    except (NoSuchElementException, TimeoutException):
        phone = "NA"
    
    if len(elements) > 1 :
        email = elements[len(elements)-1].text
    else :
        email = "NA"

    # print("phone is", phone)
    # print("email is", email)
    
    return email, phone

    

   
            
