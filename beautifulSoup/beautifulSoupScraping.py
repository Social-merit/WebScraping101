from bs4 import BeautifulSoup
import requests

#===================================================#
# Extracting the links of multiple movie transcripts
#==================================================#

# Get The HTML
root = 'https://subslikescript.com'  # homepage of the website
website = f'{root}/movies'  # concatenating the homepage with the movies section
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())  # prints the HTML of the website

# Locate the box that contains a list of movies
box = soup.find('article', class_='main-article')

# Store each link in "links" list (href doesn't consider root aka "homepage", so we have to concatenate it later)
links = []
for link in box.find_all('a', href=True):  # find_all returns a list
    links.append(link['href'])

#================================================#
# Extracting the movie transcript
#================================================#

# Loop through the "links" list and sending a request to each link
for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Locate the box that contains title and transcript
    box = soup.find('article', class_='main-article')
    # Locate title and transcript
    title = box.find('h1').get_text()
    title = ''.join(title.split('/'))
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    # Exporting data in a text file with the "title" name
with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)




#####################################################
# Extracting links from pagination bar
#####################################################

# How To Get The HTML
root = 'https://subslikescript.com'  # this is the homepage of the website
website = f'{root}/movies_letter-X'  # concatenating the homepage with the movies "letter-X" section. You can choose any section (e.g., letter-A, letter-B, ...)
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# Locate the box that contains the pagination bar
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text  # this is the number of pages that the website has inside the movies "letter X" section

##################################################################################
# Extracting the links of multiple movie transcripts inside each page listed
##################################################################################

# Loop through all tbe pages and sending a request to each link
for page in range(1, int(last_page)+1):
    result = requests.get(f'{website}?page={page}')  # structure --> https://subslikescript.com/movies_letter-X?page=2
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Locate the box that contains a list of movies
    box = soup.find('article', class_='main-article')

    # Store each link in "links" list (href doesn't consider root aka "homepage", so we have to concatenate it later)
    links = []
    for link in box.find_all('a', href=True):  # find_all returns a list
        links.append(link['href'])

    #################################################
    # Extracting the movie transcript
    #################################################

    for link in links:
        try:  # "try the code below. if something goes wrong, go to the "except" block"
            result = requests.get(f'{root}/{link}')  # structure --> https://subslikescript.com/movie/X-Men_2-290334
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            # Locate the box that contains title and transcript
            box = soup.find('article', class_='main-article')
            # Locate title and transcript
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            # Exporting data in a text file with the "title" name
            with open(f'{title}.txt', 'w') as file:
                file.write(transcript)
        except:
            print('------ Link not working -------')
            print(link)




'''
import requests
import os
import time
from bs4 import BeautifulSoup

# Create a folder to save the PDFs
folder_name = 'PDFs'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/105.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
   
}

root = 'https://appunti.cavallium.it'
# Navigate to the webpage and find the PDF URLs using BeautifulSoup
website_url = f'{root}/Algebra%20e%20Geometria'
response = requests.get(website_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

box = soup.find('tbody')

print(box)

# Find the PDF URL
pdf_url = None
for link in box.find_all('a', href=True):
    if '.pdf' in link['href']:
        pdf_url = link['href']
        print(pdf_url)
        break

# Download the PDF using requests
if pdf_url:
    pdf_response = requests.get(f'{website_url}/{pdf_url}', headers=headers)
    pdf_file_path = os.path.join(folder_name, 'file.pdf')  # Save the PDF in the created folder
    with open(pdf_file_path, 'wb') as f:
        f.write(pdf_response.content)



# Download multiple PDF using requests
# pdf_urls = []
# for link in box.find_all('a', href=True):
#     if '.pdf' in link['href']:
#         pdf_urls.append(link['href'])

# # Download the PDFs using requests
# for i, pdf_url in enumerate(pdf_urls):
#     pdf_response = requests.get(f'{website_url}/{pdf_url}', headers=headers)
#     pdf_file_path = os.path.join(folder_name, f'file_{i + 1}.pdf')  # Save the PDF in the created folder with a unique name
#     with open(pdf_file_path, 'wb') as f:
#         f.write(pdf_response.content)
#     time.sleep(5)  # Wait for 2 seconds before the next request
#     print(f'File {i + 1} downloaded successfully!')

# print('All PDFs downloaded successfully!')





'''