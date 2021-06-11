# This program prints Hello, world!

import requests
import json
import sys

BASE_URL_GET_TOKEN = 'https://apis.goflipr.com/OAuth2/token?grant_type=password&password=Ght1v%26l0&username=duprefm@gmail.com'
BASE_URL_GET_DATA = 'https://apis.goflipr.com/modules/1A1C74/survey/LastHours/24'
token = ""
username = "duprefm@gmail.com"
password = "Ght1v&l0"

payload = {
    'grant_type': 'password',
    'username': username,
    'password': password
}

r = requests.post("https://apis.goflipr.com/OAuth2/token",
    headers={"Content-Type":"application/x-www-form-urlencoded"},
    data=payload)

json_data = r.json()

x = json.dumps(json_data, indent=4, sort_keys=True)

y = json.loads(x)
token = (y["access_token"])

headers = {'Authorization': "Bearer {}".format(token)}
auth_response = requests.get(BASE_URL_GET_DATA, headers=headers)

#print(auth_response.json())

with open('FliprData.json', 'w') as f:
    print(auth_response.json(), file=f)