import requests
import http.client
import ssl
import os
import json

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

def sendtoSCPI(message):
    #---- User specific (read from file) --------------------
    with open('setting.json', "r") as jsonfile:
        settings = json.load(jsonfile)

    certificate_file = settings['certificate_file']
    pfx_file = settings['pfx_file']
    password = settings['password']
    url = settings['url']
    client_id = settings['client_id']
    client_secret = settings['client_secret']
    token_url = settings['token_url']
    api_url = settings['api_url']
#--------------------------------------------------------

#--------TEST DATA ------------------------
    data = {"TestTag" : "TestValue"}
    #sample_payload = json.dumps(data) --- to use test data and ignore inbound data ..,...
    sample_payload = json.dumps({"query" : message})
#------------------------------------------

# Create an OAuth2Session object with the client credentials
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

# Use the OAuth2Session object to make requests to the service
    response = oauth.post(api_url, data=sample_payload ,headers={'Accept': 'application/json'})

# Print the response content
    return response.content
