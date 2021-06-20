'''
Created by: SamP
Date: 11-Jun-2021
Python module to pull Yelp data from 3 endPoints - business search, Business detail and Review
'''
import json
import requests
import secret_yelp
from random import randrange
import loggingM
import datafunctions
import pandas as pd


dfunc = datafunctions
job_nm = 'data_collection'
pid =dfunc.get_max_id(job_nm)
pid = pid+1
#start logging
dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Started Successfully')
i= randrange(3)
limit=2#randrange(51)
#offset=#randrange(51)
print('### '+datafunctions.dttime+'\n### No of recs: '+str(limit))
file_loc="C:\\Users\\samy8\\Desktop\\Work Lab\\SpringBoard\\github\\dataengineering\\capstone\\data\\LandingZone\\"

sort = ['best_match', 'rating', 'review_count']#to randomize the data
sort_by=sort[i]
location = 'NYC,NY'
base_url = 'https://api.yelp.com/v3/'
bus_url = base_url+'businesses/search'
bus_dtl_url = base_url + 'businesses/'
headers = {'Authorization': 'Bearer {}'.format(secret_yelp.token)}
payload = {'location':location,'limit':limit,'term': 'restaurant','sort_by':sort_by} #50 is the limit
#API Calls
response = requests.get(bus_url,headers=headers, params=payload,timeout=2)
if response.status_code ==200:
	d=json.loads(response.content)
	loggingM.logging.info(str(limit)+' Business records extracted. sorted_by: '+sort_by)
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
				#print(ddd)
				dd['pid']=pid
				dd['LoadDTTM']=datafunctions.dttime
				bdtl_key = ['id','name','alias','is_claimed','is_closed','url','phone','display_phone','review_count','categories','rating','location','coordinates','price','hours','transactions','pid','LoadDTTM'] #only pulling these attributes and reordering
				dd =  {k:dd.get(k,None) for k in bdtl_key}
				ddd['pid']=pid
				ddd['LoadDTTM']=datafunctions.dttime
				ddd['bus_id']=str(bus['id'])
				rvw_key = ['bus_id','reviews','LoadDTTM','pid'] #only pulling these attributes and reordering
				ddd =  {k:ddd.get(k,None) for k in rvw_key}
				rvw_str.append(ddd)
			else:
				print ('error while calling '+ bus_dtl_url+str(bus['id'])+'/reviews' )
				dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Failed error while calling '+ bus_dtl_url+str(bus['id'])+'/reviews')
		else:
			print ('error while calling '+ bus_dtl_url+str(bus['id']) )
			dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Failed error while calling '+ bus_dtl_url)
else:
	print ('Bad Request - '+response.status_code)
	dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Failed')

#generate data files
try:
	dfunc.export_df(dtl_str,'bus_dtl')
	loggingM.logging.info('Business details records extract complete.Total extracted = '+ str(limit))
	dfunc.export_df(rvw_str,'rvw_dtl')
	loggingM.logging.info('Review details records extract complete')
	dfunc.flattenjson(rvw_str,'rvw_dtl')
	loggingM.logging.info('Review details records flattening complete')
	dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Total business records extracted = '+ str(limit))
	dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Completed Successfully')
	loggingM.logging.info('Python Execution Completed Successfully!')
except Exception as e1:
	loggingM.logging.info('Record extract failed.' + str(e1))
	dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Failed. Check Log for more info')
	
#to-do
#real time app 
#rvw data needs to be pivoted before adding
# as no of col changes from one load to another it is causing issues while doing cdc
# dont run in less than 1 min interval
# include process id and datetime insertion



