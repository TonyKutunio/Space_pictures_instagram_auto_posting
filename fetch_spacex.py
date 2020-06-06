import requests
import os
from PIL import Image
import utils
from functools import partial


def fetch_spacex_launch_urls(launch_number):
    spacex_url = 'https://api.spacexdata.com/v3/launches/{}'.format(launch_number)
    response = requests.get(spacex_url)
    response.raise_for_status()
    unpacked_response = response.json()
    spacex_pictures_urls = unpacked_response['links']['flickr_images']
    return spacex_pictures_urls

if __name__ == "__main__":
    launch_number = 'latest'
    folder_path = 'Instagram_auto_posting/Space Pictures/'
    spacex_pictures_urls = fetch_spacex_launch_urls(launch_number)
    mission = 'spacex'
    image_id = 0
    download_pictures_partial = partial(utils.download_pictures, folder_path, spacex_pictures_urls, image_id, mission)

    download_pictures_partial()
    utils.thumbnail_pictures(folder_path)
