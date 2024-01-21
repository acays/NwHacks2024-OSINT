from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_profile(driver, profiles) :
    for profile in profiles :
        print("profile link is", profile)
        driver.get(profile)
        wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Contact info']")))
        element.click()