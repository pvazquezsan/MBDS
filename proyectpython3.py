import krakenex
from pykrakenapi import KrakenAPI
import plotly.graph_objects as go
import pandas as pd
import matplotlib
import virtualenv as virtualenv #para colgar en internet puntos extras
import krakenex #conectar al servidor de kraken
from pykrakenapi import KrakenAPI #conectar a la base de datos
import plotly.graph_objects as go #graficos basketball
import time #tiempo de intervalos de datos

#ohlc DataFrame
api = krakenex.API()
k = KrakenAPI(api)
coins = ["ZRXUSD","BCHUSD","XZECZUSD"]
BCHUSD,last= k.get_ohlc_data("BCHUSD",interval=1440)# 60 min *24  horas. last es el ultimo valor de la columna time
# si no lo descargamos se baja
# todo como tupla
BCHUSD=BCHUSD.reset_index()
time.sleep(.9)

ZRXUSD,last= k.get_ohlc_data("ZRXUSD",interval=1440)#60 min *24  horas
ZRXUSD=ZRXUSD.reset_index()
time.sleep(.9)

XZECZUSD,last= k.get_ohlc_data("XZECZUSD",interval=1440)#60 min *24  horas
XZECZUSD=XZECZUSD.reset_index()
print(type(BCHUSD))

##CANDLESTICK "ZRXUSD","BCHUSD","XZECZUSD"
df_dtime = pd.DataFrame({
    'ZRXUSD': ZRXUSD['dtime'],
    'BCHUSD': BCHUSD['dtime'],
    'XZECZUSD': XZECZUSD['dtime']
})
df_open = pd.DataFrame({
    'ZRXUSD': ZRXUSD['open'],
    'BCHUSD': BCHUSD['open'],
    'XZECZUSD': XZECZUSD['open']
})
df_high = pd.DataFrame({
    'ZRXUSD': ZRXUSD['high'],
    'BCHUSD': BCHUSD['high'],
    'XZECZUSD': XZECZUSD['high']
})
df_low = pd.DataFrame({
    'ZRXUSD': ZRXUSD['low'],
    'BCHUSD': BCHUSD['low'],
    'XZECZUSD': XZECZUSD['low']
})
df_close = pd.DataFrame({
    'ZRXUSD': ZRXUSD['close'],
    'BCHUSD': BCHUSD['close'],
    'XZECZUSD': XZECZUSD['close']
})

fig = go.Figure()

for coin in coins:
    fig.add_trace(
        go.Candlestick(x=df_dtime[coin],
                       open=df_open[coin],
                       high=df_high[coin],
                       low=df_low[coin],
                       close=df_close[coin],
                       name = coin)
    )
    fig.update_layout(
        updatemenus=[go.layout.Updatemenu(
            active=0,
            buttons=list(
                [dict(label='All',
                      method='update',
                      args=[{'visible': [True, True, True]},
                            {'title': 'All',
                             'showlegend': True}]),
                 dict(label='ZRXUSD',
                      method='update',
                      args=[{'visible': [True, False, False]},
                            # the index of True aligns with the indices of plot traces
                            {'title': 'ZRXUSD',
                             'showlegend': True}]),
                 dict(label='BCHUSD',
                      method='update',
                      args=[{'visible': [False, True, False]},
                            {'title': 'BCHUSD',
                             'showlegend': True}]),
                 dict(label='XZECZUSD',
                      method='update',
                      args=[{'visible': [False, False, True]},
                            {'title': 'XZECZUSD',
                             'showlegend': True}]),
                 ])
        )
        ])

fig.show()

    #CANDLESTICK
'''fig = go.Figure(data=[go.Candlestick(x=ohlc['dtime'],
                    open=ohlc['open'],
                    high=ohlc['high'],
                    low=ohlc['low'],
                    close=ohlc['close'])])
fig.show()

for coin in coins():
    fig.add_trace(
        go.Scatter(
            x=df_stocks.index,
            y=df_stocks[column],
            name=column
        )
    )
'''
#############