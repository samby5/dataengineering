import pandas as pd
import collections
import requests
import secret
location = 'NYC,NY'
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'Bearer {}'.format(secret.token)}
payload = {'location':location,'limit':2,'term': 'restaurant'}
response = requests.get(url,headers=headers, params=payload,timeout=2)
if response.status_code ==200:
	print(response.text)
