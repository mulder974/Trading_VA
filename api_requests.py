from datetime import datetime
import calendar
import pandas as pd
import time


import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
from pybit import HTTP 



def connexion_to_API():

    load_dotenv(find_dotenv())

    API_KEY = os.environ.get("API_KEY", "default")
    API_SECRET_KEY = os.environ.get("API_SECRET", "default")

    session = HTTP(endpoint="https://api.bybit.com",
                    api_key=API_KEY,
                    api_secret=API_SECRET_KEY
    )
    print("Bot API session created !" )

    return session



#access old data with the link : https://public.bybit.com/premium_index/BTCUSD/

def get_last_data(session, symbol):

    
    while True:

        now = datetime.utcnow()
        unixtime = calendar.timegm(now.utctimetuple())
        since = unixtime - 300 * 200   # Here current time minus 5 min * 200 rows so 1000 minutes before now


        print(f"\n data requested at : {now}")

        #response from bybit
        response = session.query_kline(symbol=symbol, interval="5", from_time=since)['result']
        
        
        df = pd.DataFrame(response)
        df = df[['symbol','open_time','close','volume','high','low']]

        df['open_time'] = df['open_time'].apply(lambda timestamp: datetime.fromtimestamp(timestamp))
        
        print(unixtime)
        print(df)
        time.sleep(60)



def get_all_data(session,symbol):
    pass



