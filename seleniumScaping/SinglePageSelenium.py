from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import urllib.request

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path='./../../../../../../Download/CV/chromedriver/chromedriver.exe')

# Open the website
driver.get("https://appunti.cavallium.it/Logica/")

# Wait for the page to load
time.sleep(2)

def clean_filename(filename):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '-')
    return filename[:250]  # Truncate file names that are too long
# //*[@id="list"]/tbody/tr[2]/td[1]/a

# Loop over each link to click and navigate
idx = 0
while True:
    # Re-fetch the links each time
    CourseLinks = driver.find_elements(By.XPATH, "//tbody/tr/td/a")
    if idx >= len(CourseLinks):
        break

    CourseLink = CourseLinks[idx]
    folder_name = clean_filename(CourseLink.text) # Create a valid folder name from the text

    CourseLink.click()
    time.sleep(2)  # wait for page to load

    # Create a new folder for each page
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Locate "tbody" and find all tr/td with class "link"
    tbody_inner = driver.find_element(By.XPATH, "//tbody")
    pdf_links = tbody_inner.find_elements(By.XPATH, "./tr/td[contains(@class, 'link')]/a")
    

        # Loop over each pdf link to download
    for pdf_idx, pdf_link in enumerate(pdf_links):
        pdf_url = pdf_link.get_attribute('href')
        pdf_text = clean_filename(pdf_link.text)
        pdf_name = os.path.join(folder_name, f"{pdf_text}.pdf")
        
        

            # Download and save the PDF
        urllib.request.urlretrieve(pdf_url, pdf_name)
        
    # Navigate back to the initial page
    driver.back()
    time.sleep(2)  # wait for page to load

    idx += 1  # increment the index

# Close the driver
driver.quit()

# ========================================================================================================