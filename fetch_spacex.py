import requests
import os
from PIL import Image
import utils
from pathlib import Path

    
def fetch_spacex_launch_urls(launch_number):
    spacex_url = 'https://api.spacexdata.com/v3/launches/{}'.format(launch_number)
    response = requests.get(spacex_url)
    response.raise_for_status()
    unpacked_response = response.json()
    spacex_pictures_urls = unpacked_response['links']['flickr_images']
    return spacex_pictures_urls

if __name__ == "__main__":
    launch_number = 'latest'
    folder_path = (Path.cwd() / 'Space Pictures')
    mission = 'spacex'
    image_id = 0
    pictures_urls = fetch_spacex_launch_urls(launch_number)
    picture_request_response = utils.get_pictures(pictures_urls, mission)


    utils.download_pictures(picture_request_response, folder_path, pictures_urls, mission, image_id)
    utils.thumbnail_pictures(folder_path)
