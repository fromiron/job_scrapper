import requests
from bs4 import BeautifulSoup
import csv
import re


word = 'python'
remoteok = f'https://remoteok.io/remote-{word}-jobs'
remoteok_db = []

print(remoteok)

request = requests.get(remoteok)
soup = BeautifulSoup(request.text, "html.parser")
soup_table = soup.find("table", {"id": "jobsboard"})
soup_table_list = soup_table.findAll("tr", {"class": "job"})

for row in soup_table_list:
    url_source = row.select('.company_and_position')
    url_wrap = re.findall(r'href=[\'"]?([^\'" >]+)', str(url_source))
    company = row.find('h3').text
    title = row.find('h2').text
    url = url_wrap[0]
    dic = {'company': company,
           'title': title,
           'url': url
           }
    remoteok_db.append(dic)
    print(dic)
