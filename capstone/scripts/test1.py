from numpy.core import records
import pandas as pd



import pandas as pd
import json
from flatten_json import flatten_json #as fj
file_loc="C:\\Users\\samy8\\Desktop\\Work Lab\\SpringBoard\\github\\dataengineering\\capstone\\data\\LandingZone\\"

df=pd.read_csv(file_loc+"rvw_dtl_20210618-0641.csv",index_col=False)
df=pd.concat([df.reviews.apply(pd.Series), df.drop('reviews', axis=1)], axis=1)
print(df)

#rvw_dict=df.to_dict()#(orient='records')
#rvw_dict=[{'a':3} ,{'a':5}]
#df_flat = pd.DataFrame(rvw_dict)
#print(rvw_dict)
#df_flat = pd.DataFrame([flatten_json(rvw_dict[k]) for k in rvw_dict.keys()])
#print(df_flat)

#st=['rvw_id','bus_id','reviews_text','user']

print(df['reviews'].to_string())
#print(pd.json_normalize(df))
#print(rvw_dict)
#df = pd.DataFrame([flatten_json(x) for x in rvw_dict])
#df.to_csv(file_loc+'new_rvw_dtl_flat.csv',mode='w', header=True,index=False)
