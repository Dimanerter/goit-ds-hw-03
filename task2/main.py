import requests
from bs4 import BeautifulSoup
import json

MAIN_URL = "https://quotes.toscrape.com/"


def get_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


def serch_authors_information(soup, list_authors_name, list_authors):
    authors = soup.find_all("small", class_="author")
    for author in authors:
        soup = get_html(MAIN_URL + author.find_next("a")["href"])
        if soup.find("h3", class_="author-title").get_text() not in list_authors_name:
            list_authors_name.append(soup.find("h3", class_="author-title").get_text())
            list_authors.append(
                {
                    "fullname": list_authors_name[-1],
                    "born_date": soup.find(
                        "span", class_="author-born-date"
                    ).get_text(),
                    "born_location": soup.find(
                        "span", class_="author-born-location"
                    ).get_text(),
                    "description": soup.find(
                        "div", class_="author-description"
                    ).get_text(),
                }
            )
    return list_authors_name, list_authors


def serch_qoutes_information(soup, list_qoutes):
    qoutes = soup.find_all("span", class_="text")
    for qoute in qoutes:
        list_qoutes.append(
            {
                "tags": [
                    tag.get_text() for tag in qoute.find_next("div").find_all("a")
                ],
                "author": qoute.find_next("small", class_="author").get_text(),
                "qoute": qoute.get_text(),
            }
        )
    return list_qoutes


soup = get_html(MAIN_URL)
next_page = 1
list_authors = []
list_authors_name = []
list_qoutes = []
while True:
    list_authors_name, list_authors = serch_authors_information(
        soup, list_authors_name, list_authors
    )
    list_qoutes = serch_qoutes_information(soup, list_qoutes)
    next_page += 1
    soup = get_html(MAIN_URL + f"/page/{next_page}/")
    if soup.find("li", class_="next") is None:
        break

with open("authors.json", "w") as file:
    json.dump(list_authors, file)

with open("qoutes.json", "w") as file:
    json.dump(list_qoutes, file)
