import requests
import urllib.request
import os
from auth import get_headers

def download_images():
    # Gets meta data about images from Message Broker
    response = requests.get('https://my.farmbot.io/api/images', headers=get_headers())
    images = response.json()

    # print(json.dumps(latestImage, indent=2))

    # Change path depending on user
    dest_direc = "./images/"

    # Saves the url's image to a folder
    for index, i in enumerate(images):
        filename = dest_direc + str(i['id']) + ".jpg"
        print(filename)

        urllib.request.urlretrieve(i["attachment_url"], filename)
        if index>8:
            break


download_images()
