"""Holds the session header and other global variables."""
import sys
import os

from requests import Session

# Keeps track on if the user is logged in or not.
LOGGED_IN = False
# The session object for making get and post requests.
SESSION = Session()
SESSION.headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json;charset=UTF-8',    
    }

OUTPUT=sys.stdout
