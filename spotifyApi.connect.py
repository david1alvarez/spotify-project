import requests
from getpass import getpass

clientId = '1bef273e723c4710b8befe9933f7aa36'
privateKey = getpass('private key:')
# nonassociated URI for auth purposes only
redirectUri = "https://spotify-project/callback/"

# url = 'https://api.spotify.com/v1/users/daveyavarez'

authUrl = 'https://accounts.spotify.com/authorize'
# userName = input("username:")
# password = getpass('password:')
params = [{'client_id': clientId, 'response_type': 'code', 'redirect_uri': redirectUri}]
import json
paramsJson = json.dumps(params)
r = requests.get(authUrl, data=paramsJson)
print(r.status_code)
