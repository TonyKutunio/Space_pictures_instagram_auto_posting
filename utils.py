import requests
import os
from PIL import Image

def download_pictures(folder_path, url, image_id, mission):
    os.makedirs(folder_path, exist_ok=True)
    if mission == 'hubble':
        response = requests.get(url)
        response.raise_for_status()

        file_extension = os.path.splitext(url)[-1]
        filename = 'HubblePicture ID {}{}'.format( + image_id, file_extension)
        with open(folder_path + filename, 'wb') as file:
            file.write(response.content)
    elif mission == 'spacex':
        for picture_number, picture_url in enumerate(url):
            response = requests.get(picture_url)
            response.raise_for_status()
            filename = 'SpaceX_flight pic{}.jpg'.format( picture_number + 1)
            with open(folder_path + filename, 'wb') as file:
                file.write(response.content)

def thumbnail_pictures(folder_path):
    file_names = os.listdir(folder_path)
    for file in file_names:
        image = Image.open(folder_path + file)
        image.thumbnail((1080, 1080))
        image.save(folder_path + file, format='JPEG')




