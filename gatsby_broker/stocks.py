from gatsby_broker.urls import *
from gatsby_broker.helper import *
import json


@login_required
def get_quotes(inputSymbols):
    
    """
    Takes any number of stock tickers and returns information pertaining to its price.

    """
    symbols = inputs_to_set(inputSymbols)
    _get_symbol = symbols.pop()
    url = quotes_url()
    load_tickers = {'word': _get_symbol}
    payload = json.dumps(load_tickers)
    data = request_post(url, payload)
    return data['response']




@login_required
def get_historical_quotes(inputSymbols,timeFrame):
    """
    This uses the MarketData. Specify the ticker symbol and the function will return the latest price. 
    TimeFrame = ["D1" ,"W1","M1",'M3', "Y1","ALL"]


    """
    symbols = inputs_to_set(inputSymbols)
    _get_symbol = symbols.pop()
    url = marketData(_get_symbol)
    load_tickers = {'timeframe': timeFrame}
    data = request_get(url, load_tickers)
    return data
    





