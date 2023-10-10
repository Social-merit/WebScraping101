
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import urllib.request

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path='./../../../../../../Download/CV/chromedriver/chromedriver.exe')

# Open the website
driver.get("https://appunti.cavallium.it/")

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







"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request

# Initialize the Chrome driver
# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='./../../../../../../Download/CV/chromedriver/chromedriver.exe')
# Open the website
driver.get("https://appunti.cavallium.it/")

# Wait for the page to load
time.sleep(2)

# Locate "tbody" elements and find all clickable links
# //tbody/tr/td/a
# tbody = driver.find_element(By.XPATH, "//*[@id='1ist']/tbody")
rows = driver.find_elements(By.XPATH, "//tbody/tr/td/a")

# Loop over each link to click and navigate
for row in rows:
    row.click()
    time.sleep(4)  # wait for page to load
    
    # Locate "tbody" and find all tr/td with class "link"
    tbody_inner = driver.find_element(By.XPATH, "//tbody")
    pdf_links = tbody_inner.find_elements(By.XPATH, "./tr/td[contains(@class, 'link')]/a")
    
    # Loop over each pdf link to download
    for idx, pdf_link in enumerate(pdf_links):
        pdf_url = pdf_link.get_attribute('href')
        pdf_name = f"page_{idx}.pdf"
        
        # Download and save the PDF
        urllib.request.urlretrieve(pdf_url, pdf_name)
        
    # Navigate back to the initial page
    driver.back()
    time.sleep(4)  # wait for page to load

# Close the driver
driver.quit()



# /html/body/main/div/div[2]/table/tbody/tr[1]/td[1]  # to find the xpath of the first page link in the table
# //font[contains(text(),'Algebra and Geometry/')]

"""





"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os

# Initialize ChromeDriver
driver = webdriver.Chrome(executable_path='./../../../../../../Download/CV/chromedriver/chromedriver.exe')

# Navigate to the initial URL
driver.get('https://appunti.cavallium.it/')

# Find and click on each link in the first tbody
tbody_rows = driver.find_elements(By.XPATH, '//*[@id="1ist"]/tbody/tr')
for row in tbody_rows:
    link = row.find_element(By.XPATH, 'td[1]/a')
    link.click()
    
    # Wait for the new page to load
    time.sleep(5)
    
    # Get all the PDF links on the new page
    pdf_links = driver.find_elements(By.XPATH, '//tbody//tr/td[contains(@class, "link")]/a')
    for pdf_link in pdf_links:
        pdf_url = pdf_link.get_attribute('href')
        
        # Download and save the PDF
        pdf_data = requests.get(pdf_url).content
        with open(f"{pdf_link.text}.pdf", "wb") as f:
            f.write(pdf_data)
            
    # Navigate back to the initial page
    driver.back()
    
    # Wait before next iteration
    time.sleep(2)

# Close the browser
driver.quit()

"""
