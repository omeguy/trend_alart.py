import MetaTrader5 as mt
import pandas as pd
import pandas_ta as ta
from datetime import datetime
import requests
import ccxt
import numpy as np

mt.initialize()

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1057814315475947571/X1Nv65Jo6o-VlIov7LYymif__Z5dF60sAe7AnLeKtgPjUJ9LaKF7f8Xk6AraOcaCNsLg"
webhook_url = "https://discordapp.com/api/webhooks/1057818187946795159/NdjTK9xfSx9_yNKqAnrWi47vgacROikJa5yiOZdLqsYdA91nPhdNIFCJbN3uOsdd5wko"

bars = mt.copy_rates_range("USDJPY", mt.TIMEFRAME_M15, datetime(2022, 10, 10), datetime.now())
df = pd.DataFrame(bars)

bars1 = mt.copy_rates_range("EURUSD", mt.TIMEFRAME_M15, datetime(2022, 10, 10), datetime.now())
df1 = pd.DataFrame(bars1)

exchange = ccxt.binance()

bars2 = exchange.fetch_ohlcv('BTCUSDT', timeframe='15m', limit=500)
df2 = pd.DataFrame(bars2, columns=['time', 'open', 'high', 'low', 'close', 'vol'])
df2['time'] = pd.to_datetime(df['time'])

exchange1 = ccxt.binance()

bars3 = exchange1.fetch_ohlcv('ETHUSDT', timeframe='15m', limit=500)
df3 = pd.DataFrame(bars3, columns=['time', 'open', 'high', 'low', 'close', 'vol'])
df3['time'] = pd.to_datetime(df['time'])

fma = df.ta.sma(length=21)
sma = df.ta.sma(length=50)
tma = df.ta.sma(length=200)
adx = df.ta.adx()

df = pd.concat([df, fma, sma, tma, adx], axis=1)

fma1 = df1.ta.sma(length=21)
sma1 = df1.ta.sma(length=50)
tma1 = df1.ta.sma(length=200)
adx1 = df1.ta.adx()

df1 = pd.concat([df1, fma1, sma1, tma1, adx1], axis=1)

fma2 = df2.ta.sma(length=21)
sma2 = df2.ta.sma(length=50)
tma2 = df2.ta.sma(length=200)
adx2 = df2.ta.adx()

df2 = pd.concat([df2, fma2, sma2, tma2, adx2], axis=1)

fma3 = df3.ta.sma(length=21)
sma3 = df3.ta.sma(length=50)
tma3 = df3.ta.sma(length=200)
adx3 = df3.ta.adx()

df3 = pd.concat([df3, fma3, sma3, tma3, adx3], axis=1)

last_row = df.iloc[-1]
last_row

last_row1 = df1.iloc[-1]
last_row1

last_row2 = df2.iloc[-1]
last_row2

last_row3 = df3.iloc[-1]
last_row3

def istrend(df):
    if last_row['SMA_200'] > last_row['SMA_50'] and last_row['SMA_50'] > last_row['SMA_21'] and last_row['ADX_14'] >=20:
         message = f"**USDJPY**:DOWNTREND:The trend:**MAY_GO_SHORT**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(webhook_url, json=payload)
        
    elif last_row['SMA_200'] < last_row['SMA_50'] and last_row['SMA_50'] < last_row['SMA_21'] and last_row['ADX_14'] >=20:
         message = f"**USDJPY**:UPTREND:The trend:**MAY_GO_LONG**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(webhook_url, json=payload)
    
    else:
         message = f"**USDJPY**:NO_CLEAR_TREND:**N**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(webhook_url, json=payload)
    

def istrend1(df1):
    if last_row1['SMA_200'] > last_row1['SMA_50'] and last_row1['SMA_50'] > last_row1['SMA_21'] and last_row1['ADX_14'] >=20:
         message = f"**EURUSD**:DOWN_TREND:The trend:**MAY_GO_SHORT**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(webhook_url, json=payload)
        
    elif last_row1['SMA_200'] < last_row1['SMA_50'] and last_row1['SMA_50'] < last_row1['SMA_21'] and last_row1['ADX_14'] >=20:
         message = f"**EURUSD**:UP_TREND:The trend:**MAY_GO_LONG**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(webhook_url, json=payload)
    
    else:
         message = f"**EURUSD**:NO_CLEAR_TREND:**N**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(webhook_url, json=payload)

    
def istrend2(df2):
    if last_row2['SMA_200'] > last_row2['SMA_50'] and last_row2['SMA_50'] > last_row2['SMA_21'] and last_row2['ADX_14'] >=20:
         message = f"**BTCUSDT**:DOWNTREND:The trend:**MAY_GO_SHORT**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
        
    elif last_row2['SMA_200'] < last_row2['SMA_50'] and last_row2['SMA_50'] < last_row2['SMA_21'] and last_row2['ADX_14'] >=20:
         message = f"**BTCUSDT**:UPTREND:The trend:**MAY_GO_LONG**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
    
    else:
         message = f"**BTCUSDT**:NO_CLEAR_TREND:**N**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
    

def istrend3(df3):
    if last_row3['SMA_200'] > last_row3['SMA_50'] and last_row3['SMA_50'] > last_row3['SMA_21'] and last_row3['ADX_14'] >=20:
         message = f"**ETHUSDT**:DOWNTREND:The trend:**MAY_GO_SHORT**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
        
    elif last_row3['SMA_200'] < last_row3['SMA_50'] and last_row3['SMA_50'] < last_row3['SMA_21'] and last_row3['ADX_14'] >=20:
         message = f"**ETHUSDT**:UPTREND:The trend:**MAY_GO_LONG**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
    
    else:
         message = f"**ETHUSDT**:NO_CLEAR_TREND:**N**"
         print(message)
         payload = {
             "username": "Trend_alartBot",
             "content": message
             
         }
         requests.post(WEBHOOK_URL, json=payload)
    

istrend3(df)
istrend3(df1)
istrend3(df2)
istrend3(df3)