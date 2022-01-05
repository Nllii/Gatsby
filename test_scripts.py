import gatsby_broker as gatsby
import pprint
from pathlib import Path
import toml 

credentials = toml.load(Path("Gatsby_keys.toml"))
id_= credentials['login_']

def test_gatsby_login():
    return_data = gatsby.login(id_['login'], id_['pass'])
    # pprint.pprint(return_data)




def test_get_account_info():
    returned_data = gatsby.load_account()
    pprint.pprint(returned_data.json())
    


def test_load_portfolio():
    returned_data = gatsby.portfolio()
    # pprint.pprint(returned_data.json())






def test_market_order():
    data = gatsby.market_buy_order(symbol='F', quantity=1,timeInForce='Day',longShort='Long',multiplier=1)
    print(data)
    # symbol, quantity, timeInForce='gtc', extendedHours=False, jsonify=True)
    # pass








test_gatsby_login()
# test_get_account_info()
# test_load_portfolio()
test_market_order()

# get_quote()



