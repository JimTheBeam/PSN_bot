from bs4 import BeautifulSoup
import logging
import requests
from time import sleep

#FIXME: I think that more elegant solution exists
import sys
sys.path.append('..')
from PSN_bot.config import Config

from utils import get_html, get_content, get_pages_count

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
        games = []
        for page in range(1, pages + 1):
            print(f'Parsing page {page} from {pages}.....')

            html = get_html(url=url, headers=HEADERS, params={'platform': platform,'page': page})
            games.extend(get_content(html.text))
            # sleep()
        print(len(games))
    else:
        print('Error')
    
if __name__ == "__main__":
    parse_main_page(url=GAMES_URL, platform='PS5')