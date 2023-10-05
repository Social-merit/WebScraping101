import requests
import os
from bs4 import BeautifulSoup


# Create a folder to save the PDF
folder_name = 'PDFs'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# https://appunti.cavallium.it/Algebra%20e%20Geometria/

root = 'https://appunti.cavallium.it'
website_url = f'{root}/Algebra%20e%20Geometria'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

response = requests.get(website_url, headers=headers)


# response = requests.get(website_url)
soup = BeautifulSoup(response.content, 'html.parser')


box = soup.find('tbody')


pdf_urls = []
for link in box.find_all('a', href=True):
    if '.pdf' in link['href']:
        pdf_urls.append(link['href'])

# Download the PDFs using requests
for i, pdf_url in enumerate(pdf_urls):
    # result = requests.get(f'{website_url}/{pdf_url}')
    pdf_response = requests.get(f'{website_url}/{pdf_url}')
    pdf_file_path = os.path.join(folder_name, f'file_{i + 1}.pdf')  # Save the PDF in the created folder with a unique name
    with open(pdf_file_path, 'wb') as f:
        f.write(pdf_response.content)



