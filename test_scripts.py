import gatsby_broker as gatsby
import pprint
from pathlib import Path
import toml 

credentials = toml.load(Path("Gatsby_keys.toml"))
id_= credentials['login_']
test_tickers = ["ABUS","EFOI","NUZE","ARQT","VRCA","OBSV","RETA","HRTX","FENC","OMER","SPRO","BYSI","AQST","LEGN"]



def test_gatsby_login():
    return_data = gatsby.login(id_['login'], id_['pass'])
    # pprint.pprint(return_data)




def test_get_account_info():
    returned_data = gatsby.load_account()
    pprint.pprint(returned_data.json())
    


def test_load_portfolio():
    returned_data = gatsby.portfolio()
    # pprint.pprint(returned_data.json())




def test_market_buy():
    for i in test_tickers:
        data = gatsby.market_buy_order(symbol=i , quantity=1,timeInForce='Day',longShort='Short',multiplier=1)
        print(data)


own_ticker = ["AAPL"]

def test_market_sell():
    for i in own_ticker:
        data = gatsby.market_sell_order(symbol=i , quantity=1,timeInForce='Day',multiplier=1)
        print(data)



def test_get_quotes():
    for i in test_tickers:
        data = gatsby.get_quotes(inputSymbols=i)
        print(data)


def test_historical_quotes():
    TimeFrame = ["D1" ,"W1","M1",'M3', "Y1","ALL"]
    for tickers in test_tickers:
        for time_frame in TimeFrame:
            print(time_frame)
            data = gatsby.get_historical_quotes(inputSymbols=tickers, timeFrame=time_frame)
            pprint.pprint(data.json())










test_gatsby_login() 
# test_historical_quotes()
# test_get_quotes()
# test_get_account_info()
# test_load_portfolio()
# test_market_buy()
# test_market_sell()




