'''
Created by: SamP
Date: 14-Jun-2021
Python refining module to refine Yelp data after extraction

'''
import json
import requests
import secret_yelp
from random import randrange
import loggingM
import datafunctions
import pandas as pd

dfunc = datafunctions
job_nm = 'data_refining'
file_loc="C:\\Users\\samy8\\Desktop\\Work Lab\\SpringBoard\\github\\dataengineering\\capstone\\data\\LandingZone\\"

pid =dfunc.get_max_id('data_collection')
dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Started Successfully')

#review data processing
try:
	df=pd.read_csv(file_loc+"rvw_dtl_flat_20210619-0721",index_col=False)
	rvw_dict=df.to_dict(orient='records')
	for k,v in rvw_dict:

	#print(rvw_dict)
	df_flat = dfunc.flattenjson(rvw_dict,'rvw_dtl')
	print(df_flat)
	'''dfunc.unpivot(df_flat,'[1:27]')
	loggingM.logging.info('Review details records extract complete - - bus dtls extract')'''
except Exception as e:
	loggingM.logging.info('Review details records extract failed')
	dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Failed - rvw dtls extract.' + str(e))

'''
try:
	dfunc.cdc_csv('bus_dtl','id')
	loggingM.logging.info('change data capture of business details record complete')
except Exception as e:
	loggingM.logging.info('Change data capture of business details record failed')
	dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Failed - cdc business details.' + str(e))
try:
	dfunc.cdc_csv('rvw_dtl','value')
	loggingM.logging.info('change data capture of review details records complete')
except Exception as e:
	loggingM.logging.info('Change data capture of review details record failed')
	dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'Job Failed - cdc review details.' + str(e))
	
	
dfunc.run_log(int(pid),job_nm,dfunc.current_dttime(),'JobEnded Successfully')
loggingM.logging.info('Python Execution Completed Successfully!')
'''