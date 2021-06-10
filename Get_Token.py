# This program prints Hello, world!

import requests
import json

BASE_URL = 'https://apis.goflipr.com/modules/1A1C74/survey/last'
token = "eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiZHVwcmVmbUBnbWFpbC5jb20iLCJzdWIiOiJkdXByZWZtQGdtYWlsLmNvbSIsIm5iZiI6MTYyMzI3MzQyMiwiZXhwIjoxNjQ2NjAxNDIyLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0LyIsImF1ZCI6IkFueSJ9.toikTjcbG7Sq9qYVeMowAXpXiCz6FAoMcpmb_S4HPwQ"

headers = {'Authorization': "Bearer {}".format(token)}
auth_response = requests.get(BASE_URL, headers=headers)

print(auth_response.json())

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y)
