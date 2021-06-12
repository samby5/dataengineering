import pandas as pd
import collections
import json
import requests
import secret
location = 'NYC,NY'
base_url = 'https://api.yelp.com/v3/'
bus_url = base_url+'businesses/search'
bus_dtl_url = base_url + 'businesses/'
headers = {'Authorization': 'Bearer {}'.format(secret.token)}
payload = {'location':location,'limit':2,'term': 'restaurant'}
response = requests.get(bus_url,headers=headers, params=payload,timeout=2)
if response.status_code ==200:
	d=json.loads(response.content)
	with open(r"C:\Users\samy8\Desktop\Work Lab\SpringBoard\github\dataengineering\Capstone\Step Three-DataCollection\json_data.txt",'w', encoding="utf-8") as f:
			f.write(str(d['businesses'])+'\n\n')
	for bus in d['businesses']:
		response = requests.get(bus_dtl_url+str(bus['id']),headers=headers,timeout=2)
		dd=json.loads(response.content)
		with open(r"C:\Users\samy8\Desktop\Work Lab\SpringBoard\github\dataengineering\Capstone\Step Three-DataCollection\json_data.txt",'a', encoding="utf-8") as f:
			f.write(str(dd)+'\n\n')