from datetime import datetime
import calendar
import pandas as pd
import time






def get_last_data(session,symbol):
    
    while True:

        now = datetime.utcnow()
        unixtime = calendar.timegm(now.utctimetuple())
        since = unixtime - 60 * 5 * 200   # Here current time minus 5 min * 200 rows so 1000 minutes before now


        print(f"data requested at : {now}")

        #response from bybit
        response = session.query_kline(symbol=symbol, interval="1", from_time=since)['result']
        
        
        df = pd.DataFrame(response)
        df = df[['symbol','open_time','close','volume']]

        print(unixtime)
        print(df)
        time.sleep(300)



def get_all_data(session,symbol):
    pass

