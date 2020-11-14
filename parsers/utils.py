from bs4 import BeautifulSoup
import logging
import requests

from pprint import pprint

def get_html(url, headers=None, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r


def get_current_price(item):
    price_tag = item.find('span', class_='content__game_card__price__current')
    if price_tag is None:
        return None
    else:
        return price_tag.get_text().replace('\xa0', '')



def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-6 col-sm-4 col-md-3 col-lg-3 col-xl-2')

    games = []
    for item in items:
        games.append({
            'title': item.find('span', class_='title').get_text(),
            'current_price': get_current_price(item)
            # 'ps_plus_price': item.find('span', class_='content__game_card__price_plus').get_text() if not None else None
        })

    pprint(games)
    
    
    