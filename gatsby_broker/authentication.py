import json
from gatsby_broker.urls import *
from gatsby_broker.helper import *


def login(username = None, password = None):
    """
    Logs in the user and returns the access token.
    """

    data = {

        'deviceType': 'IOS',
        'login': username,
        'pass': password,

    }

    url = login_url()
    data = request_post(url, payload= json.dumps(data))
    return data



