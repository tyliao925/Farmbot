import requests
import urllib.request
# Grabs API Token using log in information
def get_token_encoded():
    global token
    token = None
    if not token:
        # Get your FarmBot Web App token.
        headers = {'content-type': 'application/json'}

        # Log in information
        user = {'user': {'email': "jiroach@ucdavis.edu", 'password': "ebs170FB"}}
        response = requests.post('https://my.farmbot.io/api/tokens',
                                 headers=headers, json=user)
        token = response.json()['token']['encoded']

    return token

def get_token_unencoded():
    global token
    token = None
    if not token:
        # Get your FarmBot Web App token.
        headers = {'content-type': 'application/json'}

        # Log in information
        user = {'user': {'email': "jiroach@ucdavis.edu", 'password': "ebs170FB"}}
        response = requests.post('https://my.farmbot.io/api/tokens',
                                 headers=headers, json=user)
        token = response.json()['token']['unencoded']

    return token

# Grabs authorization headers with the API token
def get_headers():
    headers = {'Authorization': 'Bearer ' + get_token_encoded(),
               'content-type': "application/json"}
    return headers