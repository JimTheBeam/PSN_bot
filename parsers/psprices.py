from bs4 import BeautifulSoup
import logging
import requests
from time import sleep

#FIXME: I think that more elegant solution exists
import sys
import os
path_to_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(path_to_parent_dir)


# import sys
# sys.path.append('..')
from config import Config

from utils import get_html, get_content, get_pages_count, insert_games_in_db

#TODO: logging!!!

URL_PS4 = Config.URL_PS4
URL_PS5 = Config.URL_PS5
GAMES_URL = Config.GAMES_URL
HEADERS = Config.HEADERS


def parse_main_page(url, platform='PS4'):
    """<platfom> must be 'PS4' or 'PS5' only"""
    html = get_html(url=url, headers=HEADERS, params={'platform': platform})
    if html.status_code == 200:
        pages = get_pages_count(html.text)
        for page in range(1, pages + 1):
            print(f'Parsing page {page} from {pages}.....')

            html = get_html(url=url, headers=HEADERS, params={'platform': platform,'page': page})
            games_on_page = get_content(html.text)
            # sleep()
            # save in db
            insert_games_in_db(games_on_page)
    else:
        print('Error status code is:', html.status_code)
    
if __name__ == "__main__":
    parse_main_page(url=GAMES_URL, platform='PS4')