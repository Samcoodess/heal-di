# healdi_main/secrets.py
import os
import configparser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRETS_FILE = os.path.join(BASE_DIR, 'secrets.txt')

config = configparser.ConfigParser()
config.read(SECRETS_FILE)

OPENCAGE_API_KEY = config.get('secrets', 'opencage_api_key')
