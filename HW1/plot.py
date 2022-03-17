# pip install yfinance

import yfinance as yf
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt


# import RUA closing prices since 3 Jan 2011
RUA = yf.Ticker('^RUA')
RUA_daily = RUA.history(interval='1d', start='2011-01-03')
RUA_monthly = RUA.history(interval='1mo', start='2011-01-03')


BTC = yf.Ticker('BTC-USD')
BTC_daily = BTC.history(interval='1d', start='2011-01-03')
BTC_monthly = BTC.history(interval='1mo', start='2011-01-03')

RUA_daily = RUA_daily['Close']        # only need close column, now it is a series
RUA_monthly = RUA_monthly['Close']    
BTC_daily = BTC_daily['Close']
BTC_monthly = BTC_monthly['Close']

# convert both to dataframe, this should be cleaned up, it is done poorly
RUA_daily = pd.DataFrame(RUA_daily)
RUA_monthly = pd.DataFrame(RUA_monthly)
BTC_daily = pd.DataFrame(BTC_daily)
BTC_monthly = pd.DataFrame(BTC_monthly)

RUA_daily['Returns'] = RUA_daily['Close'].pct_change()
RUA_monthly['Returns'] = RUA_monthly['Close'].pct_change()
BTC_daily['Returns'] = BTC_daily['Close'].pct_change()
BTC_monthly['Returns'] = BTC_monthly['Close'].pct_change()

 
def plot_histogram(daily_returns, title):
    daily_returns.hist(bins=50, histtype='bar', color='blue')
    mean = daily_returns.mean()
    std = daily_returns.std()
 
    plt.axvline(x=mean, color='r', linestyle='--')
    plt.axvline(x=std, color='k', linestyle='--')
    plt.axvline(x=-std, color='k', linestyle='--')
    plt.ylabel('Frequency')
    plt.xlabel(f'Returns of: {title}')
     
    plt.show()
 
plot_histogram(RUA_daily['Returns'], 'RUA daily')
plot_histogram(RUA_monthly['Returns'], 'RUA monthly')
plot_histogram(BTC_daily['Returns'], 'BTC daily')
plot_histogram(BTC_monthly['Returns'], 'BTC monthly')
