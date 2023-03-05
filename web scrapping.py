import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}
    url=f'https://merojob.com/category/it-telecommunication/?page=1'
    r=requests.get(url,headers)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup

def transform(soup):
    divs=soup.find_all('div',class_ = 'col-8 col-lg-9 col-md-9 pl-3 pl-md-0 text-left')
    for item in divs:
        title=item.find('a').text.strip()
        company=item.find('h3',class_='h6').text.strip()
        location=item.find('span',itemprop='addressLocality').text.strip()
        job={
            'Title':title,
            'Company':company,
            'Location':location

        }
        joblist.append(job)
    return

joblist=[]

for i in range(0,6,6):
    print(f'Getting pages,{i}')
    c=extract(1)
    transform(c)

df=pd.DataFrame(joblist)
df.to_csv('Jobs.csv')