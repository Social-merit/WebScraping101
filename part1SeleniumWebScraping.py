###############################################################################################################
# ==================  Scraping football data from a website using Selenium and Python part 1 ==================
###############################################################################################################


 # ================================= Importing libraries =================================
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pandas as pd
import time




 # ================================= Set path for chromedriver.exe  and website =================================

path = './../../../../../Download/CV/chromedriver/chromedriver.exe'
# Define the website to scrape and path where the chromedriver is located
website = 'https://www.adamchoi.co.uk/overs/detailed'



# =============================  Selenium driver initialization  ==========================================
service = Service(executable_path=path) # Responsible for starting the ChromeDriver server
driver = webdriver.Chrome(service=service) # instance of chrome driver
driver.get(website) # to open the website in the browser


# ================================== Locate and click on a button ==================================
# //*[@id="page-wrapper"]/div/div[3]/div/div/div/label[1]
all_matches_button = driver.find_element('xpath', '//*[@id="page-wrapper"]/div/div[3]/div/div/div/label[1]') # to select over 1.5
all_matches_button.click() # to click on the button

# //*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]
# all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
all_matches_button = driver.find_element('xpath', '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]') # to select All matches
all_matches_button.click() # to click on the button


time.sleep(1)

# (1) England, premier league,  2023-24


# ===================   Select dropdown and select element inside by visible text  ===================
# //*[@id="country"]
dropdown = Select(driver.find_element('id', 'country')) # to select the dropdown country
dropdown.select_by_visible_text('England')

# //*[@id="league"]
dropdown = Select(driver.find_element('id', 'league')) # to select the dropdown league
dropdown.select_by_visible_text('Premier League')

# //*[@id="season"]
dropdown = Select(driver.find_element('id', 'season')) # to select the dropdown season
dropdown.select_by_visible_text('23/24')


time.sleep(2)


# ============================== from the table to list storage: looping through the table to the matche list ==============================

matches = driver.find_elements('xpath', '//tr') # to select all the matches in the table

date = []
home_team = []
score = []
away_team = []

for match in matches: # looping through the matches
    date.append(match.find_element('xpath', './td[1]').text) # to select the date of the match in the table
    home = match.find_element('xpath', './td[2]').text # to select the home team of the match in the table
    home_team.append(home)
    score.append(match.find_element('xpath', './td[3]').text) # to select the score of the match in the table
    away_team.append(match.find_element('xpath', './td[4]').text) # to select the away team of the match in the table

driver.quit() # to close the driver



# =================================  Create DataFrame in Pandas and export to CSV  =================================

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team}) # to create a DataFrame in Pandas with the data looped from the table in the website

df.to_csv('EnglandPremierLeague202324Football_data.csv', index=False) # to export the DataFrame to a CSV file


print('Dataframe created and exported to CSV') # to print a message
print(df) # to print the DataFrame
