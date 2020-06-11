import requests
import os
from PIL import Image
import utils
from pathlib import Path


def fetch_hubble_launch_url(image_id):
    hubble_url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(hubble_url)
    response.raise_for_status()
    unpacked_response = response.json()
    http_prefix = 'http:'
    full_hubble_image_url = http_prefix+unpacked_response['image_files'][-1]['file_url']
    return full_hubble_image_url

if __name__ == "__main__":
    image_id = 1
    folder_path = (Path.cwd() / 'Space Pictures')
    mission = 'hubble'
    picture_url = fetch_hubble_launch_url(image_id)
    picture_request_response = utils.get_pictures(picture_url, mission)

    utils.download_pictures(picture_request_response, folder_path, picture_url, mission, image_id)
    utils.thumbnail_pictures(folder_path)

