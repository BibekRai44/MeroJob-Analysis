import requests
from bs4 import BeautifulSoup
import csv

urls = ['https://merojob.com/category/it-telecommunication/?page={}'.format(page) for page in range(1, 11)]

with open('hrefs.txt', 'w') as file:

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        parent_links = soup.find_all('h1', class_='text-primary font-weight-bold media-heading h4')
        for parent_link in parent_links:
            children = parent_link.find('a')
            href_value = "https://merojob.com"+children.get('href')
            file.write(href_value + '\n')