from gatsby_broker.stocks import *
from gatsby_broker.urls import *
from gatsby_broker.profiles import *
import toml 
import pathlib as Path
import os




@login_required
def portfolio():
    if os.path.exists(Path.Path(os.getcwd()) / 'session.toml'):
        with open(Path.Path(os.getcwd()) / 'session.toml', 'r') as f:
            apex_account = toml.load(f)
            try:
                if apex_account['apex_account']:
                    return apex_account
                    # print('Apex_account found')
                else:
                    print('No Apex _account found')
                    pass
            except Exception as e:
                print('saving Account number to session file, call the function again ')
                account_detail = load_account()
                account_info = account_detail.json()
                apex_account['apex_account'] = account_info['response']['apexAccount']
                toml.dump(apex_account, open(Path.Path(os.getcwd()) / 'session.toml', 'w'))
                return apex_account

    
