import pandas as pd
from datetime import datetime
import os
from flatten_json import flatten_json

file_loc="C:\\Users\\samy8\\Desktop\\Work Lab\\SpringBoard\\github\\dataengineering\\capstone\\data\\LandingZone\\"
ext='csv'#file extension
dttime=datetime.now().strftime("%Y%m%d-%H%M") #datetime

def export_df(s,file_nm):
	'''Take a list of dictionaries and output a csv file '''
	print(s)
	df=pd.DataFrame(s)
	df.to_csv(file_loc+file_nm+'_'+dttime+'.'+ext,index=False,mode='w',header=True)
	 
#function to compare two csvs and consoldate into final csv
def cdc_csv(file_nm,cdc_col):
	df_i = pd.read_csv(file_loc+file_nm+'_'+dttime+'.'+ext)
	#df_i = pd.read_csv(file_loc+file_nm+tgt+dttime+'.'+ext)
	check = True  if os.path.isfile(file_loc+file_nm+'_final'+'.'+ext) else False
	if check == False:
		df_i.to_csv(file_loc+file_nm+'_final'+'.'+ext,mode='w', header=True,index=False)
	else:
		df_out = pd.read_csv(file_loc+file_nm+'_final'+'.'+ext )
		#print(df_out)
		if file_nm == 'rvw_dtl':
			cdc_col_list = list(df_out[df_out['variable'].isin(['reviews_0_id','reviews_1_id','reviews_2_id']) ][cdc_col])
		else:
			cdc_col_list = list(df_out[cdc_col])
		new_str=[]
		for row in df_i.itertuples():			
			if getattr( row,cdc_col) not in cdc_col_list:
				new_str.append(row[1:])
				#print(new_str)
		df_write = pd.DataFrame(new_str)
		# dont write this df_new = df_out.append(df_i,ignore_index=True, sort=False)
		df_new = df_write.append(df_i,ignore_index=True, sort=False)
		#print(df_write)
		df_new.to_csv(file_loc+file_nm+'_final'+'.'+ext,mode='a', header=False,index=False)
	
def flattenjson(data_dict,file_nm):
	'''	flatten a list of dictionary	Help:https://stackoverflow.com/questions/58442723/how-to-flatten-a-nested-json-recursively-with-flatten-json'''
	df_write = pd.DataFrame([flatten_json(i) for i in data_dict])
	df_write.to_csv(file_loc+file_nm+'_flat_'+dttime+'.'+ext,mode='a', header=True,index=False)
	return df_write

#take list of dictionaries in row-formatand, unpivot based on col position,   and generate csv file
#this function is only used for rvw dtl
def unpivot(dframe_flat,cols_pos):
	#df=pd.DataFrame(data)
	df=dframe_flat
	col_list=list(df.columns)
	new_df = pd.melt( df,['bus_id','LoadDTTM','pid'],col_list[1:28])#col_pos not working
	new_df.to_csv(file_loc+'rvw_dtl'+'_'+dttime+'.'+ext,index=False)
	
def run_log(id, job_nm,dttm , msg):
	df= pd.DataFrame([{'batch_id':id,'job_nm':job_nm,'datetime':dttm , 'message':msg}])
	if os.path.exists(file_loc+'job_runs'+'.'+ext):
		df.to_csv(file_loc+'job_runs'+'.'+ext,header=False,index=False,mode='a')
	else:
		df.to_csv(file_loc+'job_runs'+'.'+ext,header=True,index=False)

def get_max_id(job_nm):
	if os.path.exists(file_loc+'job_runs'+'.'+ext):
		df = pd.read_csv(file_loc+'job_runs'+'.'+ext )
		return df[df['job_nm'] == job_nm]['batch_id'].max()
	else:
		return 0

def current_dttime():
	return datetime.now().strftime("%Y%m%d-%H%M")
'''
#function to compare to csvs and consoldate into final csv
def cdc(file_nm):
	df_i = pd.read_csv(file_loc+file_nm+'_' +dttime+'.'+ext)
	check = True  if os.path.isfile(file_loc+file_nm+'_final'+'.'+ext) else False
	if check == False:
		df_i.to_csv(file_loc+file_nm+'_final'+'.'+ext,mode='w', header=True,index=False)
	else:
		df_out = pd.read_csv(file_loc+file_nm+'_final'+'.'+ext )
		df_write = pd.merge(df_i, df_out, on='id')
		print(df_write)
		df_write.to_csv(file_loc+file_nm+'_final'+'.'+ext,mode='a', header=False,index=False)
'''


