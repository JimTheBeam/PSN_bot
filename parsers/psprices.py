from bs4 import BeautifulSoup
import logging
import requests
import yaml

from pprint import pprint

try:
    stream = open('config.yaml', 'r')
except FileNotFoundError:
    print('File not found!')
except PermissionError:
    print('Permission error!')
data = yaml.safe_load(stream)
URL_PS4 = data.get('psprices_config').get('URL').get('PS4')
HEADERS = data.get('psprices_config').get('HEADERS')
print(URL_PS4)
print(HEADERS)
# pprint(data)