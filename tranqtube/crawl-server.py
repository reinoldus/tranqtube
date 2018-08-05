import requests
import urllib.parse
from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


supported_extensions = ["mp4", "webm"]


def crawl(address):
    videos = []
    items = requests.get(address).json()

    for item in items:
        name = urllib.parse.quote(item["name"], safe='')

        if item['type'] == "directory":
            new_address = address + name + "/"

            # Go into directory by recursive call
            dir_videos = crawl(new_address)

            videos.extend(dir_videos)

        elif item['type'] == "file" and name.split(".")[-1] in supported_extensions:
            clean_name = urllib.parse.unquote(address + name).replace(server_ip, "")
            videos.append({
                "path": clean_name.split("/"),
                "file_name": clean_name.split("/")[-1],
                "full_web_path": address + name
            })

    return videos


if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
    server_ip = os.getenv("VIDEO_SERVER_IP", "http://localhost:44445/")

    print("Looking for videos on: ", server_ip)

    from tranqtube.default_settings import MONGO
    client = MongoClient(MONGO)
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
