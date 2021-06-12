'''
Created by: SamP
Date: 11-Jun-2021
Python module to pull Yelp data from 3 endPoints - business search, Business detail and Review
'''
import pandas as pd
import json
import requests
import secret
import logging
from datetime import datetime
from random import randrange
i= randrange(3)
limit=randrange(51)
dttime=datetime.now().strftime("%Y%m%d-%H%M") #datetime
print(dttime)
ext='csv'#file extension
file_loc="C:\\Users\\samy8\Desktop\\Work Lab\\SpringBoard\\github\\dataengineering\\Capstone\\Step Three-DataCollection\\LandingZone\\"
log_loc="C:\\Users\\samy8\Desktop\\Work Lab\\SpringBoard\\github\\dataengineering\\Capstone\\Step Three-DataCollection\\LandingZone\\log\\"
logging.basicConfig(filename=log_loc+'YelpAPIDataCollect_'+dttime+'.log',level=logging.INFO,
					format='%(asctime)s:%(levelname)s:%(message)s')
sort = ['best_match', 'rating', 'review_count']#to randomize the data
sort_by=sort[i]
location = 'NYC,NY'
base_url = 'https://api.yelp.com/v3/'
bus_url = base_url+'businesses/search'
bus_dtl_url = base_url + 'businesses/'
#funtion to create dataframe and then export in csv
def export_df(s,file_nm):
	df=pd.DataFrame(s)
	df.to_csv(file_loc+file_nm+'_'+dttime+'.'+ext,index=False,mode='w')
headers = {'Authorization': 'Bearer {}'.format(secret.token)}
payload = {'location':location,'limit':limit,'term': 'restaurant','sort_by':sort_by} #50 is the limit
response = requests.get(bus_url,headers=headers, params=payload,timeout=2)
if response.status_code ==200:
	d=json.loads(response.content)
	export_df(d['businesses'],'bus')
	logging.info(str(limit)+' Business records extracted. sorted_by: '+sort_by)
	dtl_str=[]
	rvw_str=[]
	for bus in d['businesses']:
		response = requests.get(bus_dtl_url+str(bus['id']),headers=headers,timeout=2)
		if response.status_code ==200:
			response_r = requests.get(bus_dtl_url+str(bus['id'])+'/reviews',headers=headers,timeout=2)
			if response.status_code ==200:
				dd=json.loads(response.content)
				ddd=json.loads(response_r.content)
				dtl_str.append(dd)
				rvw_str.append(ddd['reviews'])
			else:
				print ('error while calling '+ bus_dtl_url+str(bus['id'])+'/reviews' )
		else:
			print ('error while calling '+ bus_dtl_url+str(bus['id']) )
else:
	print ('Bad Request - '+response.status_code)

export_df(dtl_str,'bus_dtl')
logging.info('Business details records extracted')
export_df(rvw_str,'rvw_dtl')
logging.info('Review details records extracted')