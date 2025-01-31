import requests
from bs4 import BeautifulSoup
import csv
import re

weworkremotely = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="

wework_db = []


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
        locaton = soup.find("span", {"class": "region"}).text
        time = soup.find(
            "span", {"class": "region"}
        ).previous_sibling.previous_sibling.text
        dic = {
            "company": company,
            "title": title,
            "locaton": locaton,
            "time": time,
            "url": url,
        }
        wework_db.append(dic)
    return wework_db
