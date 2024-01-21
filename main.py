from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from scrape_profile import scrape_profile
import time
import re
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
    

def find_users_with_job(driver, num_profiles_r) :
    driver.get("https://www.google.com")
    search_query = driver.find_element(By.NAME, "q")

    search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')
    search_query.send_keys(Keys.RETURN)
    profile_links = []
    while len(profile_links) < num_profiles_r :
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
        
        html_content = driver.page_source

        profile_links = find_links(html_content, r'https://\w+\.linkedin\.com/in/\w+', num_profiles_r)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        
    return profile_links

def find_links(html_content, regex_pattern, num_profiles_r) :
    matches = re.findall(regex_pattern, html_content)

    unique_matches = list(set(matches))

    return unique_matches

if __name__ == "__main__" :

    # Initialize the WebDriver (Chrome)
    driver = webdriver.Chrome()

    login(driver)
    num_profiles_r = 5
    profile_links = find_users_with_job(driver, num_profiles_r)

    scrape_profile(driver, profile_links)
    driver.quit()
