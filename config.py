import os
import yaml


base_dir = os.path.abspath(os.path.dirname(__file__))
config_path = base_dir + '/config.yaml'


# TODO: change print to logging
try:
    # FIXME: need to close file!
    with open(config_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print('Error in configuration file:', e)
except FileNotFoundError:
    print('config file not found!')
except PermissionError:
    print('Permission error!')


# print(data)

class Config(object):
    BOT_TOKEN = data.get('bot_config').get('BOT_TOKEN')
    URL_PS4 = data.get('psprices_config').get('URL').get('PS4')
    URL_PS5 = data.get('psprices_config').get('URL').get('PS5')
    ABS_URL = data.get('psprices_config').get('URL').get('ABS_URL')
    GAMES_URL = data.get('psprices_config').get('URL').get('GAMES_URL')
    HEADERS = data.get('psprices_config').get('HEADERS')

    START_DB_NAME = data.get('database_config').get('START_DB_NAME')
    DB_NAME = data.get('database_config').get('DB_NAME')
    DB_USER = data.get('database_config').get('DB_USER')
    DB_HOST = data.get('database_config').get('DB_HOST')
    DB_PASSWORD = data.get('database_config').get('DB_PASSWORD')
