from gatsby_broker.urls import *
from gatsby_broker.helper import *
import toml
import os
import pathlib as path
import json




@login_required
def market_buy_order(symbol, quantity, timeInForce='Day', longShort=None, multiplier=None):
    """Submits a market order to be executed immediately.

    """ 
    return order(symbol, quantity, "Open", timeInForce='Day', multiplier = multiplier)
    # return order(symbol, quantity, "buy", None, None, timeInForce, extendedHours, jsonify)


@login_required
def market_sell_order(symbol, quantity, timeInForce='Day', multiplier = None):
    """Submits a market order to be executed immediately.

    """ 
    return order(symbol, quantity, "Close", timeInForce='Day', multiplier = multiplier)





@login_required
def order(symbol, quantity, side, timeInForce='Day',longShort = "Long",multiplier=None):
    """A generic order function.

    :param symbol: The stock ticker of the stock to purchase.
    """ 
    try:
        symbol = symbol.upper().strip()
    except AttributeError as message:
        print("call this function in a loop")
        return None

    # strategy = "Equity"
    # if side == "buy":
    #     priceType = "ask_price"
    # else:
    #     priceType = "bid_price"

    load = {
            "strategy": "Equity",
            "openClose": side,
            "timeInForce":timeInForce,
            "quantity": quantity,
            # "limitContract": False,
            "legs": [
                {
                    "symbol": symbol,
                    "longShort": longShort,
                    "multiplier": multiplier
                }],
            # "tradeId": False,
            "paper": False

        }
    if os.path.exists(path.Path(os.getcwd()) / 'session.toml'):
        with open(path.Path(os.getcwd()) / 'session.toml') as session_file:
            session = toml.load(session_file)
        account_number = session['apex_account'] 
    else:
        pass
    payload = json.dumps(load)
    url = orders_url(ApexAccount = account_number)
    data = request_post(url, payload)
    return data

    
