from functools import wraps
# import requests
from gatsby_broker.globals import LOGGED_IN, OUTPUT, SESSION


def set_login_state(logged_in):
    """Sets the login state"""
    global LOGGED_IN
    LOGGED_IN = logged_in

def set_output(output):
    """Sets the global output stream"""
    global OUTPUT
    OUTPUT = output

def get_output():
    """Gets the current global output stream"""
    global OUTPUT
    return OUTPUT

def login_required(func):
    """A decorator for indicating which methods require the user to be logged
       in."""
    @wraps(func)
    def login_wrapper(*args, **kwargs):
        global LOGGED_IN
        if not LOGGED_IN:
            raise Exception('{} can only be called when logged in'.format(
                func.__name__))
        return(func(*args, **kwargs))
    return(login_wrapper)



def request_post(url, payload=None, timeout=16, json=False, jsonify_data=True):
    """For a given url and payload, makes a post request and returns the response. Allows for responses other than 200.

    :param url: The url to send a post request to.
    :type url: str
    :param payload: Dictionary of parameters to pass to the url as url/?key1=value1&key2=value2.
    :type payload: Optional[dict]
    :param timeout: The time for the post to wait for a response. Should be slightly greater than multiples of 3.
    :type timeout: Optional[int]
    :param json: This will set the 'content-type' parameter of the session header to 'application/json'
    :type json: bool
    :param jsonify_data: If this is true, will return requests.post().json(), otherwise will return response from requests.post().
    :type jsonify_data: bool
    :returns: Returns the data from the post request.

    """
    data = None
    res = None
    try:
        if json:
            update_session('Content-Type', 'application/json')
            res = SESSION.post(url, json=payload, timeout=timeout)
            update_session(
                
                'Content-Type', 'application/json;charset=UTF-8')
        else:
            res = SESSION.post(url, data=payload, timeout=timeout)
        data = res.json()
    except Exception as message:
        print("Error in request_post: {0}".format(message), file=get_output())
    # Either return response <200,401,etc.> or the data that is returned from requests.
    if jsonify_data:
        return(data)
    else:
        return(res)

    # 'Accept': 'application/json',
    # 'Content-Type': 'application/json;charset=UTF-8',
    # 'client-device-model': 'Apple iPhone X',
    # 'client-version': '2.30.5-IOS',
    # 'client-device-os-version': '14.0',




def update_session(key, value):
    """Updates the session header used by the requests library.

    :param key: The key value to update or add to session header.
    :type key: str
    :param value: The value that corresponds to the key.
    :type value: str
    :returns: None. Updates the session header with a value.

    """
    SESSION.headers[key] = value

def round_price(price):
    """Takes a price and rounds it to an appropriate decimal place that Robinhood will accept.

    :param price: The input price to round.
    :type price: float or int
    :returns: The rounded price as a float.

    """
    price = float(price)
    if price <= 1e-2:
        returnPrice = round(price, 6)
    elif price < 1e0:
        returnPrice = round(price, 4)
    else:
        returnPrice = round(price, 2)

    return returnPrice

