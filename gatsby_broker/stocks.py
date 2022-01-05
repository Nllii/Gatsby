from gatsby_broker.urls import *
from gatsby_broker.helper import *
import json


@login_required
def get_quotes(inputSymbols):
    
    """Takes any number of stock tickers and returns information pertaining to its price.
    tickers = ["AAPL","AMZN","GOOG","MSFT"]
    def get_quote():
    for i in tickers:
        return_data = gatsby.stocks.get_quotes(inputSymbols = i)    
        print(return_data)

    """
    symbols = inputs_to_set(inputSymbols)
    _get_symbol = symbols.pop()
    url = quotes_url()
    load_tickers = {'word': _get_symbol}
    payload = json.dumps(load_tickers)
    data = request_post(url, payload)
    return data['response']









