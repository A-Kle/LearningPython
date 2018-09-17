from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os.path

def start_search():
    search = input("Search for:")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    url = "https://www.bing.com/images/search"
    r = requests.get(url, params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1] #title
            try:
                img = Image.open(BytesIO(img_obj.content))
                path = "./" + dir_name + "/" + title
                img.save(path, img.format)
            except:
                print("Could not save image.")
        except:
            print("Could not request image.")

    start_search()

start_search()