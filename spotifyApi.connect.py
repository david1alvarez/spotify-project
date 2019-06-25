import requests
from getpass import getpass
# import json
import base64

clientId = '1bef273e723c4710b8befe9933f7aa36'
privateKey = getpass('private key:')
encodedPrivateKey = base64.b64encode(privateKey.encode())
print(privateKey)
print(encodedPrivateKey)
# nonassociated URI for auth purposes only
# redirectUri = "https://spotify-project/callback/"

grantType = "client_credentials"
authUrl = 'https://accounts.spotify.com/api/token'
params = [{'grant_type':grantType}]
headers = (clientId, privateKey)
bodyParams = {'grant_type': grantType}
# paramsJson = json.dumps(params)
# headersJson = json.dumps(headers)


r = requests.post(authUrl, data=bodyParams, auth=headers)
print('status code is '+ str(r.status_code))
print('body is '+ str(r.content))
