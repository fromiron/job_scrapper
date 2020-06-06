import requests
from bs4 import BeautifulSoup
import csv

weworkremotely = 'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term='


request = requests.get(weworkremotely+'python')

soup = BeautifulSoup(request.text, "html.parser")

soup_table = soup.select(".feature")
for row in soup_table:
    company = row.find("span", {"class": "company"}).text
    title = soup.find("span", {"class": "title"}).text
    region = soup.find("span", {"class": "region"}).text
    time = soup.find("span", {"class": "region"}).previous_sibling.previous_sibling.text
    print(company)
    print(title)
    print(region)
    print(time)




