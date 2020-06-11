import requests
import os
from PIL import Image

def get_pictures( url, mission):
    if mission == 'hubble':
        response = requests.get(url)
        response.raise_for_status()
        return response
    elif mission == 'spacex':
        for picture_number, picture_url in enumerate(url):
            response = requests.get(picture_url)
            response.raise_for_status()
            return response


def download_pictures(response, folder_path, url, mission, image_id):
    os.makedirs(folder_path, exist_ok=True)
    if mission == 'hubble':
        file_extension = os.path.splitext(url)[-1]
        filename = 'HubblePicture ID {}{}'.format( + image_id, file_extension)
        with open(folder_path + filename, 'wb') as file:
            file.write(response.content)
    elif mission == 'spacex':
        for picture_number, picture_url in enumerate(url):
            filename = 'SpaceX_flight pic{}.jpg'.format( picture_number + 1)
            with open(folder_path + filename, 'wb') as file:
                file.write(response.content)



def thumbnail_pictures(folder_path):
    file_names = os.listdir(folder_path)
    for file in file_names:
        image = Image.open(folder_path + file)
        image.thumbnail((1080, 1080))
        image.save(folder_path + file, format='JPEG')

