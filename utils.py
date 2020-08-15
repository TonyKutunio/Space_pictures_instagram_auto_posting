import requests
import os
from PIL import Image

def get_pictures(url, mission):
    if mission == 'hubble':
        response = requests.get(url)
        response.raise_for_status()
        return response
    elif mission == 'spacex':
        for picture_url in url:
            response = requests.get(picture_url)
            response.raise_for_status()
            return response

def download_pictures(response, folder_path, url, mission, image_id):
    os.makedirs(folder_path, exist_ok=True)
    for picture_number, picture_url in enumerate(url):
        if mission == 'hubble':
            file_extension = os.path.splitext(url)[-1]
            filename = mission + ' {}{}'.format(image_id, file_extension)   #TODO  there are some ways to make a code more optimized 
        elif mission == 'spacex':
            filename = mission + ' {}.jpg'.format(picture_number + 1)
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)

def thumbnail_pictures(folder_path):
    file_names = os.listdir(folder_path)
    for filename in file_names:
        file_path = os.path.join(folder_path, filename)
        image = Image.open(filename)
        image.thumbnail((1080, 1080))
        image.save(file_path, format='JPEG')

