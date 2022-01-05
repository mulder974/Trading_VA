
from pybit import HTTP 

import time
from datetime import datetime
import calendar

import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
from pybit import HTTP 

import api_requests as API

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY", "default")
API_SECRET_KEY = os.environ.get("API_SECRET", "default")

session = HTTP(endpoint="https://api.bybit.com",
                api_key=API_KEY,
                api_secret=API_SECRET_KEY
)

print("Bot Connected to ByBit Api !")



API.get_last_data(session,"BTCUSD")




