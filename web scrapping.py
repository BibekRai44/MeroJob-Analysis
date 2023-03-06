import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}
    urls = ['https://merojob.com/category/it-telecommunication/?page={}'.format(page) for page in range(1, 11)]
    soup_list = []
    for url in urls:
        r=requests.get(url,headers)
        soup=BeautifulSoup(r.content,'html.parser')
        soup_list.append(soup)
    return soup_list

def transform(soup_list):
    for soup in soup_list:
        divs=soup.find_all('div',class_ = 'col-8 col-lg-9 col-md-9 pl-3 pl-md-0 text-left')
        for item in divs:
            title=item.find('a').text.strip()
            company=item.find('h3',class_='h6').text.strip()
            location=item.find('span',itemprop='addressLocality').text.strip()
            parent_span = item.find('span', {'itemprop':'skills'})
            skills = []
            if parent_span:
                children = parent_span.find_all('span', {'class': 'badge badge-pill badge-light rounded text-muted'})
                for child in children:
                    skills.append(child.get_text())
        
            job={
                'Title':title,
                'Company':company,
                'Location':location,
                'KeySkills': skills

             }
            joblist.append(job)

joblist=[]

soup_list = extract('url')
transform(soup_list)

print(joblist)
df=pd.DataFrame(joblist)
df.to_csv('Jobs.csv')
