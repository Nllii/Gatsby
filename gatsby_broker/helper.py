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
            # print(res.text)
        data = res.json()
    except Exception as message:
        print("Error in request_post: {0}".format(message), file=get_output())
    # Either return response <200,401,etc.> or the data that is returned from requests.
    if jsonify_data:
        return(data)
    else:
        return(res)

 
def request_get(url, payload):
    """ Generic function for sending a get request.

    :param url: The url to send a get request to.
    :type url: str
    :param payload: Dictionary of parameters to pass to the url. Will append the requests url as url/?key1=value1&key2=value2.
    :type payload: dict
    :param parse_json: Requests serializes data in the JSON format. Set this parameter true to parse the data to a dictionary \
        using the JSON format.
    :type parse_json: bool
    :returns: Returns a tuple where the first entry is the response and the second entry will be an error message from the \
        get request. If there was no error then the second entry in the tuple will be None. The first entry will either be \
        the raw request response or the parsed JSON response based on whether parse_json is True or not.
    """
    response_error = None
    try:
        response = SESSION.get(url, params=payload)
        print(response.text)
        response.raise_for_status()
    except Exception as e:
        
        response_error = e
    # Return either the raw request object so you can call response.text, response.status_code, response.headers, or response.json()
    # or return the JSON parsed information if you don't care to check the status codes.
    # if parse_json:
    #     return response.json(), response_error
    # else:
    #     return response, response_error






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




def filter_data(data, info):
    """Takes the data and extracts the value for the keyword that matches info.

    :param data: The data returned by request_get.
    :type data: dict or list
    :param info: The keyword to filter from the data.
    :type info: str
    :returns:  A list or string with the values that correspond to the info keyword.

    """
    if (data == None):
        return(data)
    elif (data == [None]):
        return([])
    elif (type(data) == list):
        if (len(data) == 0):
            return([])
        compareDict = data[0]
        noneType = []
    elif (type(data) == dict):
        compareDict = data
        noneType = None

    if info is not None:
        if info in compareDict and type(data) == list:
            return([x[info] for x in data])
        elif info in compareDict and type(data) == dict:
            return(data[info])
        else:
            print(error_argument_not_key_in_dictionary(info), file=get_output())
            return(noneType)
    else:
        return(data)



def inputs_to_set(inputSymbols):
    """Takes in the parameters passed to *args and puts them in a set and a list.
    The set will make sure there are no duplicates, and then the list will keep
    the original order of the input.

    :param inputSymbols: A list, dict, or tuple of stock tickers.
    :type inputSymbols: list or dict or tuple or str
    :returns:  A list of strings that have been capitalized and stripped of white space.

    """

    symbols_list = []
    symbols_set = set()

    def add_symbol(symbol):
        symbol = symbol.upper().strip()
        if symbol not in symbols_set:
            symbols_set.add(symbol)
            symbols_list.append(symbol)

    if type(inputSymbols) is str:
        add_symbol(inputSymbols)
    elif type(inputSymbols) is list or type(inputSymbols) is tuple or type(inputSymbols) is set:
        inputSymbols = [comp for comp in inputSymbols if type(comp) is str]
        for item in inputSymbols:
            add_symbol(item)

    return(symbols_list)


def error_argument_not_key_in_dictionary(keyword):
    return('Error: The keyword "{0}" is not a key in the dictionary.'.format(keyword))



def error_ticker_does_not_exist(ticker):
    return('Warning: "{0}" is not a valid stock ticker. It is being ignored'.format(ticker))
