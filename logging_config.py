import logging
from logging.handlers import RotatingFileHandler

import os


# logging.basicConfig(
    # format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
#     level=logging.INFO, filename='bot.log'
# )

# logging.info('bot started')
# logger = logging.getLogger(__name__)


if not os.path.exists('logs'):
    os.mkdir('logs')
logger = logging.getLogger(__name__)
file_handler = RotatingFileHandler('logs/PSN_bot.log', 
                                maxBytes=10240, backupCount=5)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)


logger.setLevel(logging.INFO)
logger.info('Logging startup')

