import gatsby_broker as gatsby
import pprint
from pathlib import Path
import toml 

credentials = toml.load(Path("Gatsby_keys.toml"))
id_= credentials['login_']

def test_gatsby_login():
    return_data = gatsby.login(id_['login'], id_['pass'])
    pprint.pprint(return_data)











if __name__ == "__main__":
    test_gatsby_login()
    print("loging works")
