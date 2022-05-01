import yfinance as yf
import pandas as pd
import plotly.graph_objects as go


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

def my_plot_function(df, color='Virdis', title=''):
    plot = go.Figure()
    plot.add_trace(go.Mesh3d(
            x = df['strike_price'], 
            y = df['TTM'], 
            z = df['impl_volatility'],
            colorbar_title = 'IV',
            colorscale = color, # Virdis
            # This line is the key to the color gradient!!!!
            #####
            intensity = df['impl_volatility'],   ##### <- hard to find on the internet
            #####
            opacity = 0.7,
            showscale = True))


    plot.update_layout(title=title + ' Vol Surface',
            # You have to pass this scene variable for labels, I have no idea why.
            # I can't figure out how else to make the axis labels.
            scene = dict(
            xaxis_title = 'Strike',
            yaxis_title = 'TTM',
            zaxis_title = 'IV'),
            # size
            width=600,
            height=600,
            # reduce border size
            margin=dict(l=40, r=40, b=40, t=40))
    plot.show()
