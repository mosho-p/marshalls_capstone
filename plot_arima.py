import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
import datetime


def fromts(ts):
    """
    Converts epoch time to a readable date
    """
    return datetime.datetime.fromtimestamp(ts)

def tots(dt):
    """
    Converts time of the form 'Jan 01 2020' to epoch time
    """
    return time.mktime(datetime.datetime.strptime(dt, "%b %d %Y").timetuple())

def fit_moving_average_trend(series, window=7):
    """
    Create a series of moving averages
    """
    return series.rolling(window, center=True).mean()

def plot_raw(df, ax, title=None, xcol='date', ycol='median_sell_price'):
    plt.style.use('ggplot')
    months = mdates.MonthLocator()
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.plot([fromts(t) for t in df[xcol]], df[ycol])
    if not title:
        title = df['item_name'].iloc[0]
    ax.set_title(title)
    plt.show()

def plot_moving_average(df, ax, title=None, xcol='date', ycol='median_sell_price', window=7, draw_raw=True):
    """
    Plots a moving average over the original plot.
    :param df: df
    :param ax: axis to plot on
    :param title: plot title (default: item name)
    :param xcol: (str) name of time column (default: 'date')
    :param ycol: (str) name of data column (default: 'median_sell_price')
    :param window: (int) moving average window size (default: 7 days)
    :param draw_raw: (bool) whether or not to plot raw data (default: True)
    :return:
    """
    plt.style.use('ggplot')
    months = mdates.MonthLocator()
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    if not title:
        title = df['item_name'].iloc[0]
    plt.style.use('ggplot')
    if draw_raw:
        ax.plot([fromts(t) for t in df[xcol]], df[ycol])
    ax.plot([fromts(t) for t in df[xcol]], fit_moving_average_trend(df[ycol], window), c='b')
    ax.set_title(title + ' Moving Average (' + str(window) + ' days)')
    plt.show()

def plot_resid(df, ax, title=None, xcol='date', ycol='median_sell_price', window=7):
    plt.style.use('ggplot')
    months = mdates.MonthLocator()
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.plot([fromts(t) for t in df[xcol]], fit_moving_average_trend(df[ycol], window).values - df[ycol].values)
    if not title:
        title = df['item_name'].iloc[0]
    ax.set_title(title + ' Residual Plot')
    plt.show()