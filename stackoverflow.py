import requests
from bs4 import BeautifulSoup
import csv
import re

stackoverflow = "https://stackoverflow.com/jobs?q="
stack_db = []


def stackoverflow_finder(word):
    request = requests.get(stackoverflow + word)
    soup = BeautifulSoup(request.text, "html.parser")
    soup_table = soup.select_one(".listResults")
    job_list = soup_table.findAll("div", {"class": "-job" and "js-result"})
    for row in job_list:
        title = row.select_one("div.grid--cell.fl1 > h2 > a").text
        url_str = row.select_one("div.grid--cell.fl1 > h2 > a")
        url_wrap = re.findall(r'href=[\'"]?([^\'" >]+)', str(url_str))
        url = f"https://stackoverflow.com/{url_wrap[0]}"
        company = row.select_one(
            "div.grid--cell.fl1 > h3 > span:nth-child(1)"
        ).text.strip()
        locaton = row.select_one(
            "div.grid--cell.fl1 > h3 > span.fc-black-500"
        ).text.strip()
        dic = {"company": company, "title": title, "locaton": locaton, "url": url}
        stack_db.append(dic)
    return stack_db
