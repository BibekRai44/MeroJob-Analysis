import requests
from bs4 import BeautifulSoup
with open('hrefs.txt', 'r') as f:
    hrefs = f.read().splitlines()

for href in hrefs:
    response = requests.get(href)
    soup = BeautifulSoup(response.content, 'html.parser')

divs=soup.find_all('table',class_='table table-hover m-0')
for item in divs:
    jobLevel = item.find('td').find_next_sibling('a').text
    