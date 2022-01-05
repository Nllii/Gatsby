import gatsby_broker as gatsby
import pprint
from pathlib import Path
import toml 

credentials = toml.load(Path("Gatsby_keys.toml"))
id_= credentials['login_']

def test_gatsby_login():
    return_data = gatsby.login(id_['login'], id_['pass'])
    pprint.pprint(return_data)




tickers = ["AAPL","AMZN","GOOG","MSFT"]
def get_quote():
    for i in tickers:
        return_data = gatsby.stocks.get_quotes(inputSymbols = i)
        pprint.pprint(return_data)




def market_buy():

    pass










test_gatsby_login()
get_quote()
