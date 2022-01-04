from gatsby_broker.urls import *
from gatsby_broker.helper import *



@login_required
def order_buy_market(symbol, quantity, timeInForce='gtc', extendedHours=False, jsonify=True):
    """Submits a market order to be executed immediately.

    """ 
    return order(symbol, quantity, "buy", None, None, timeInForce, extendedHours, jsonify)



@login_required
def order(symbol, quantity, side, limitPrice=None, stopPrice=None, timeInForce='gtc', extendedHours=False, jsonify=True):
    """A generic order function.

    :param symbol: The stock ticker of the stock to purchase.
    """ 
    try:
        symbol = symbol.upper().strip()
    except AttributeError as message:
        print(message, file=get_output())
        return None

    orderType = "market"
    trigger = "immediate"

    if side == "buy":
        priceType = "ask_price"
    else:
        priceType = "bid_price"

    if limitPrice and stopPrice:
        price = round_price(limitPrice)
        stopPrice = round_price(stopPrice)
        orderType = "limit"
        trigger = "stop"
    elif limitPrice:
        price = round_price(limitPrice)
        orderType = "limit"
    elif stopPrice:
        stopPrice = round_price(stopPrice)
        if side == "buy":
            price = stopPrice
        else:
            price = None
        trigger = "stop"
    else:
        price = round_price(next(iter(get_latest_price(symbol, priceType, extendedHours)), 0.00))





    # payload = {
    #     'account': load_account_profile(info='url'),
    #     'instrument': get_instruments_by_symbols(symbol, info='url')[0],
    #     'symbol': symbol,
    #     'price': price,
    #     'quantity': quantity,
    #     'ref_id': str(uuid4()),
    #     'type': orderType,
    #     'stop_price': stopPrice,
    #     'time_in_force': timeInForce,
    #     'trigger': trigger,
    #     'side': side,
    #     'extended_hours': extendedHours
    # }

    # url = orders_url()
    # data = request_post(url, payload, jsonify_data=jsonify)

    # return(data)
