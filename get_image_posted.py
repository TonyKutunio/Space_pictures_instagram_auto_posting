import os
import instabot
from instabot import Bot
from os import listdir
from dotenv import load_dotenv
from functools import partial


def get_image_posted(username, password, folder_path):
    folder_with_pictures = listdir(folder_path)
    bot = instabot.Bot()
    bot.login(username=username, password=password)

    for picture in folder_with_pictures:
        bot.upload_photo(folder_path + picture)

if __name__ == "__main__":
    load_dotenv()
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    folder_path = ('Instagram_auto_posting/Space Pictures/')
    get_image_posted_partial = partial(get_image_posted,username, password, folder_path)
    get_image_posted_partial()







