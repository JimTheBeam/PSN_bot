from bs4 import BeautifulSoup
import logging
import requests

#FIXME: I think that more elegant solution exists
import sys
sys.path.append('..')
from PSN_bot.config import Config

from utils import get_html, get_content

#TODO: logging!!!

URL_PS4 = Config.URL_PS4
URL_PS5 = Config.URL_PS5
HEADERS = Config.HEADERS


def parse_main_page_ps4():
    html = get_html(url=URL_PS4, headers=HEADERS)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')
    
if __name__ == "__main__":
    parse_main_page_ps4()