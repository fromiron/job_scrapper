import requests
from bs4 import BeautifulSoup
import csv
import re

stackoverflow = 'https://stackoverflow.com/jobs?q='

stack_db = []


def weworkremotely_finder(word):
    request = requests.get(weworkremotely + word)
    soup = BeautifulSoup(request.text, "html.parser")
    soup_table = soup.select(".feature")
    for row in soup_table:
        url_str = row.find("a")
        url_wrap = re.findall(r'href=[\'"]?([^\'" >]+)', str(url_str))
        url = url_wrap[0]
        company = row.find("span", {"class": "company"}).text
        title = soup.find("span", {"class": "title"}).text
        region = soup.find("span", {"class": "region"}).text
        time = soup.find("span", {"class": "region"}
                         ).previous_sibling.previous_sibling.text
        dic = {'company': company,
               'title': title,
               'region': region,
               'time': time,
               'url': url
               }
        wework_db.append(dic)
        print(dic)

weworkremotely_finder('javascript')

