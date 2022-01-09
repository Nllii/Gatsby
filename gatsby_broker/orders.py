from gatsby_broker.urls import *
from gatsby_broker.helper import *
import toml
import os
import pathlib as path
import json
from gatsby_broker.profiles import *
import pprint





@login_required
def market_buy_order(symbol, quantity, timeInForce='Day', longShort=None, multiplier=None):
    """
    Submits a market order to be executed immediately.

    """ 
    return order(symbol, quantity, "Open", timeInForce='Day', multiplier = multiplier,paper=False)
    # return order(symbol, quantity, "buy", None, None, timeInForce, extendedHours, jsonify)



@login_required
def market_sell_order(symbol, quantity, timeInForce='Day', multiplier = None):
    """
    Submits a market order to be executed immediately.

    """ 
    return order(symbol, quantity, "Close", timeInForce='Day', multiplier = multiplier,paper=False)



@login_required
def draft_buy(symbol, quantity, timeInForce='Day', longShort=None, multiplier=None):
    """
    Submits a paper buy order to be executed immediately.

    """
    return order(symbol, quantity, "Open", timeInForce='Day', multiplier = multiplier,paper=True)



@login_required
def draft_sell(symbol, quantity, timeInForce='Day', longShort=None, paper=True):
    """
    Submits a paper sell order to be executed immediately.

    """
    return order(symbol, quantity, timeInForce='Day', longShort=None, paper=True)
    


@login_required
def cancel_draft(all=False,symbol=None):
    """
    Cancels all open paper orders for a given symbol or a single symbol.

    """
    return cancel_paper(all=False,symbol=None)




@login_required
def order(symbol, quantity, side, timeInForce='Day',longShort = "Long",multiplier=None,paper=None):
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
            "paper": paper

        }
    if os.path.exists(path.Path(os.getcwd()) / 'session.toml'):
        with open(path.Path(os.getcwd()) / 'session.toml') as session_file:
            session = toml.load(session_file)
        account_number = session['apex_account'] 
    else:
        pass
    payload = json.dumps(load)
    if paper == True:
        paper_url = tradePaper(ApexAccount =  account_number)
        data = request_post(paper_url, payload)
        return data
    else:
        live_order = orders_url(ApexAccount =  account_number)
        data = request_post(live_order, payload)
        return data





def cancel_paper(all=False,symbol=None):
    """Cancels all open paper orders for a given symbol or a  single ticker.
    """
    if os.path.exists(path.Path(os.getcwd()) / 'session.toml'):
        with open(path.Path(os.getcwd()) / 'session.toml') as session_file:
            session = toml.load(session_file)
        account_number = session['apex_account'] 
    account_url = portfolio_url(ApexAccount =  account_number)
    account_data = request_get(account_url)
    if all == True:
        for position in account_data.json()['trades']:
            if position['paper'] == True:
                paper_url = cancel_paperOrders(ApexAccount =  account_number,  order_id = position['id'])
                data = request_delete(paper_url)
                print(data.json())
    # else:

        
