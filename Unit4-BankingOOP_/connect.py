import pyodbc
#choose between providing uid/password and Trusted_Connection
conn_str="DRIVER={SQL Server};SERVER=localhost;DATABASE=Springboard;Trusted_Connection=yes"
sql_conn = pyodbc.connect(conn_str)
cursor = sql_conn.cursor()
