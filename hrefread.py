import requests
from bs4 import BeautifulSoup
import pandas as pd

with open('hrefs.txt') as file:
    urls = [url.strip() for url in file.read().split('\n') if url.strip()]

print(f'total urls = {len(urls)}')
jobs = []

for url in urls:
    print(f'scraping url {url}')
    try:
        r = requests.get(url)
    except:
        print(f'Error scraping {url}')
        continue

    if not r.ok:
        print(f'Error scraping {url}')
        continue

    soup = BeautifulSoup(r.text, 'html.parser')

    job = {
        'job_category': '', 'job_level': '', 'no_of_vacancy': '', 'employment_type': '',
        'offered_salary': '', 'education_level': '', 'experience_required':''
    }

    for tr in soup.select('table.table tr'):
        try:
            tds = tr.select('td')
            label = tds[0].text.strip()
            value = tds[-1].text.strip()
        except:
            continue

        if 'Job Category' in label:
            job['job_category'] = value
        elif 'Job Level' in label:
            job['job_level'] = value
        elif 'Vacancy' in label:
            job['no_of_vacancy'] = value
        elif 'Employment Type' in label:
            job['employment_type'] = value
        elif 'Offered Salary' in label:
            job['offered_salary'] = value
        elif 'Education Level' in label:
            job['education_level'] = value
        elif 'Experience Required' in label:
            job['experience_required'] = value

    
    jobs.append(job)

df = pd.DataFrame(jobs)
df.to_csv('new_data.csv', index=False)


