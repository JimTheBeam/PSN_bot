from bs4 import BeautifulSoup
import logging
import requests

from db.db_game import insert_game_in_games
from config import Config

def get_html(url, headers=None, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r


def get_current_price(item):
    '''get current price from part of html document
    return None if not found'''
    price_tag = item.find('span', class_='content__game_card__price__current')
    if price_tag is None:
        return None
    else:
        current_price = price_tag.get_text().replace('\xa0', '').replace('₽', '')
        if current_price == 'Бесплатно':
            current_price = -1
        return int(current_price)


def get_plus_price(item):
    '''get ps plus price from part of html document
    return None if not found'''
    plus_price_tag = item.find('span', class_='content__game_card__price_plus')
    if plus_price_tag is None:
        return None
    else:
        plus_price = plus_price_tag.get_text().strip().replace('\xa0', '').replace('₽', '')
        if plus_price == 'Бесплатно':
            plus_price = -1
        return int(plus_price)


def get_old_price(item):
    '''get old price (if the game has a discount) from part of html document
    return None if not found'''
    old_price_tag = item.find('span', class_='old_price')
    if old_price_tag is None:
        return None
    else:
        old_price = old_price_tag.get_text().replace('\xa0', '').replace('₽', '')
        return int(old_price)


# TODO: ПЕРЕДЕЛАТЬ ЭТО ИЗ СТРОКИ В НОРМ ДАТУ!!!!
def get_discount_end_date(item):
    '''finds discount end date(if the game has a discount) from part of html document
    return None if not found'''
    end_date_tag = item.find('span', class_='content__game_card__end_date')
    if end_date_tag is None:
        return None
    else:
        return end_date_tag.get_text().strip()


def get_psprices_link(item):
    '''finds link for psprices page from part of html document
    return None if not found'''
    relative_link = item.find('a', class_='content__game_card__cover').get('href')
    abs_link = Config.ABS_URL + relative_link
    return abs_link


def get_pages_count(html):
    '''finds last page number[int] from first page and return its'''
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('ul', class_='pagination')
    last_page_link = pagination.find('li', class_='last').find('a').get('href')
    last_page_number = int(last_page_link.split('page=')[-1])
    return last_page_number


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-6 col-sm-4 col-md-3 col-lg-3 col-xl-2')
    games = []
    for item in items:
        game = {
            'title': item.find('span', class_='title').get_text(),
            'current_price': get_current_price(item),
            'plus_price': get_plus_price(item),
            'old_price': get_old_price(item),
            'image_link': item.find('img', class_='game-card--image').get('content'),
            'discount_end_date': get_discount_end_date(item),
            'psprices_url': get_psprices_link(item)
        }
        games.append(game)
    return games


def insert_games_in_db(games):
    '''insert a single game in database'''
    for game in games:
        insert_game_in_games(game)
