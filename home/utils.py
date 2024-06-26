import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .models import availability


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Function to open the webpage in headless mode
def open_webpage_headless(url, chrome_binary):
    chrome_options = Options()
    chrome_options.binary_location = chrome_binary
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.add_argument("--disable-extensions")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver

# Function to check if the word 'Studienzwecken' is present and click the continue link
def check_for_study(driver, max_retries=10):
    retries = 0
    while retries < max_retries:
        try:
            study_elements = WebDriverWait(driver, 5, poll_frequency=0.2).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Studienzwecken')]"))
            )
            for study_element in study_elements:
                continue_link = WebDriverWait(study_element, 5, poll_frequency=0.2).until(
                    EC.element_to_be_clickable((By.XPATH, "./following::a[text()='Weiter'][1]"))
                )
                continue_link.click()
                return
        except TimeoutException:
            retries += 1
            time.sleep(0.5)  # Shorter delay

# Function to click the 'New Appointment' link
def click_new_appointment(driver):
    try:
        new_appointment_link = WebDriverWait(driver, 5, poll_frequency=0.2).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Neuer Termin')]"))
        )
        new_appointment_link.click()
    except TimeoutException:
        pass
def get_appointment_url():
    availability.objects.all().delete()
    logging.info("Checking for availability...")
    url = "https://service2.diplo.de/rktermin/extern/choose_categoryList.do?locationCode=isla&realmId=108"
    chrome_binary = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    # Open the webpage in headless mode and perform initial actions
    driver = open_webpage_headless(url, chrome_binary)
    try:
        check_for_study(driver)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        click_new_appointment(driver)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        new_availability = availability(url=driver.current_url)
        new_availability.save()
        logging.info(f"Availability found: {driver.current_url}")
    finally:
        driver.quit()
