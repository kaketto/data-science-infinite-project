import pandas as pd
import numpy as np
import requests as requests
import json
from flask import Flask, render_template, redirect, request
import sys
sys.path.insert(0, '/Users/kingaeniko/greenfox/data_science_infinite_project')
import api_keys

app = Flask(__name__)

from TwitterAPI import TwitterAPI

SEARCH_TERM = '%23nordiclight'

api = TwitterAPI(api_keys.twitter_consumer_api, 
                 api_keys.twitter_consumer_secret_api,
                 api_keys.twitter_access_token,
                 api_keys.twitter_access_token_secret)

r = api.request('search/tweets', {'q': SEARCH_TERM})

for item in r:
    print( item)

print('\nQUOTA: %s' % r.get_quota())