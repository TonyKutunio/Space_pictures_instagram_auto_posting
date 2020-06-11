import os
import instabot
from instabot import Bot
from os import listdir
from dotenv import load_dotenv
from pathlib import Path


def get_image_posted(username, password, folder_path):
    folder_with_picture_names = listdir(folder_path)
    bot = instabot.Bot()
    bot.login(username=username, password=password)

    for picture_name in folder_with_picture_names:
        bot.upload_photo(folder_path + picture_name)

if __name__ == "__main__":
    load_dotenv()
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    folder_path = (Path.cwd() / 'Space Pictures')
    get_image_posted(username, password, folder_path)






