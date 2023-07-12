import requests
from bs4 import BeautifulSoup
from os import getenv
from dotenv import load_dotenv
load_dotenv()
DOMEN = getenv("DOMEN")

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}


def UpdateHtml(url, hd=HEADERS):
    response = requests.get(url, headers=hd)
    try:
        if response.status_code == 200:
            return response.text
    except:
        pass


def GetContent(res):
    soup = BeautifulSoup(res, "lxml").find("div", {"id": "dle-content"}).find_all("div", {"class": "shortstory"})
    
    data = []

    for i in soup:
        content = i.find("div", {"class": "shortstoryContent"})
        img = DOMEN + content.find("img").get("src")
        title = str(content.find("h4")).replace("<h4>", "").replace("</h4>", "")
        category = []
        for j in i.find("div", {"class": "shortstoryFuter"}).find_all("a"):
            category.append(j.text)
        desc = str(content.find("p").find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()).split("<br/>")[0].replace("<p><strong>Описание: </strong>", "")

        data.append({
            "anime_img": img,
            "anime_title": title,
            "anime_category": category,
            "anime_desc": desc
        })
    return data


def ParsAnimeDemo():
    URL = getenv("URL")
    data = []
    for i in range(1, 5):
        res = UpdateHtml(URL + str(i))
        index = GetContent(res)
        data.extend(index)
    return data