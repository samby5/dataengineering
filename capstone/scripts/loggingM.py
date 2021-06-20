import logging
from datetime import datetime
dttime=datetime.now().strftime("%Y%m%d-%H%M") #datetime
log_loc="C:\\Users\\samy8\\Desktop\\Work Lab\\SpringBoard\\github\\dataengineering\\capstone\\data\\LandingZone\\log\\"
logging.basicConfig(filename=log_loc+'YelpAPIDataCollect_'+dttime+'.log',level=logging.INFO,
					format='%(asctime)s:%(levelname)s:%(message)s')