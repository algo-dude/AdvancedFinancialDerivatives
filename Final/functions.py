import yfinance as yf
import pandas as pd

def import_data(ticker, start_date, end_date, interval):
    """
    Imports data from Yahoo Finance.
    """
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    return data

def check_contango(x, y):
    '''
    x: int
        Spot price
    y: int
        Future Price    
    '''
    return x < y

def apply_contango(df1, df2):
    '''
    Apply contango to df1.
    '''
    temp = pd.Series
    # give temp index of df1
    temp.index = df1.index
    # compare each Close price on each index
    for i in range(len(df1)):
        temp.iloc[i] = check_contango(df1.iloc[i]['Close'], df2.iloc[i]['Close'])
        
    return temp
