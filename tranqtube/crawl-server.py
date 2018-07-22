import requests
import urllib.parse
from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

server_ip = "http://144.76.3.243:44445/"
supported_extensions = ["mp4", "webm"]


def crawl(address):
    videos = []
    items = requests.get(address).json()

    for item in items:
        name = urllib.parse.quote(item["name"], safe='')

        if item['type'] == "directory":
            new_address = address + name + "/"

            videos.extend(crawl(new_address))

        elif item['type'] == "file" and name.split(".")[-1] in supported_extensions:
            clean_name = urllib.parse.unquote(address + name).replace(server_ip, "")
            videos.append({
                "path": clean_name.split("/"),
                "file_name": clean_name.split("/")[-1],
                "full_web_path": address + name
            })

    return videos

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client.tranqtube
    videos = db['videos']
    db.videos.create_index("full_web_path", unique=True)
    items = crawl(server_ip)
    for item in items:
        # This is probably not performant
        try:
            videos.insert_one(
                item
            )
        except DuplicateKeyError as e:
            pass
