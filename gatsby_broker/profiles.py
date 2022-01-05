
from gatsby_broker.stocks import *
from gatsby_broker.urls import *




@login_required
def load_account():
    url = self_account_url()
    data = request_get(url, payload = None, parse_json = None)
    return data
    # return(filter_data(data))



