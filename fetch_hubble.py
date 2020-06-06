import requests
import os
from PIL import Image
import utils
from functools import partial


def fetch_hubble_launch(image_id):
    hubble_url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(hubble_url)
    response.raise_for_status()
    unpacked_response = response.json()
    http_prefix = 'http:'
    full_hubble_image_url = http_prefix+unpacked_response['image_files'][-1]['file_url']
    return full_hubble_image_url

if __name__ == "__main__":
    image_id = 1
    folder_path = 'Instagram_auto_posting/Space Pictures/'
    mission = 'hubble'
    hubble_picture_url = fetch_hubble_launch(image_id)
    download_pictures_partial = partial(utils.download_pictures, folder_path, hubble_picture_url, image_id, mission)

    download_pictures_partial()
    utils.thumbnail_pictures(folder_path)
