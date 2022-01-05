import json
from gatsby_broker.urls import *
from gatsby_broker.helper import *
import toml 
import pathlib as Path
import os


def login(username = None, password = None, store_session = True):
    """
    Logs in the user and returns the access token.
    """

    data = {

        'deviceType': 'IOS',
        'login': username,
        'pass': password,
        # 'device_token': device_token
    }
    if store_session is False and os.path.exists(Path.Path(os.getcwd()) / 'session.toml'):
        os.remove(Path.Path(os.getcwd()) / 'session.toml')
    else:
        pass

    url = login_url()
    if os.path.exists(Path.Path(os.getcwd()) / 'session.toml'):
        session_token = get_session()['response']['token']
        # print(session_token)
        set_login_state(True)
        update_session('Authorization', 'Bearer {0}'.format(session_token))
        
    else:
        login_data = request_post(url, payload= json.dumps(data))
        if store_session is True:
            try:
                with open(Path.Path(os.getcwd()) / 'session.toml', 'w') as file:
                    toml.dump(login_data, file)
            except:

                print('Could not store session')
        else:

            print('Session not stored, login each time login() function is called.')
            if os.path.exists(Path.Path(os.getcwd()) / 'session.toml'):
                os.remove(Path.Path(os.getcwd()) / 'session.toml')
            else:
                
                print('No session file found.')
        return login_data






def get_session():    
    """
    Returns the session data.
    """
    try:
        with open(Path.Path(os.getcwd()) / 'session.toml', 'r') as file:
            session_data = toml.load(file)
            data = {
                'refreshToken':session_data['response']['refreshToken'],
                'userId': session_data['response']['userId']
            }
            # test login before saving key to header.
            url = sessiontoken_url()
            session_token = request_post(url, payload= json.dumps(data))
            if session_token['status'] == 'SUCCESS':
                print("successfully logged into gatsby")
                return session_token 
            else:
                print('Session token could not be retrieved.')
                return session_token
    except:
        print('Could not get session error from get_session() function ')
        # return None
