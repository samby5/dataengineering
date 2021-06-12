"""
Created by samy on 7-Jun-2021
Function to define connection
"""

import pyodbc

_connection = None

def get_connection(pw):
	conn_str="DRIVER={SQL Server};SERVER=localhost;DATABASE=Springboard;Trusted_Connection=yes"
	sql_conn = pyodbc.connect(conn_str)
	cursor = sql_conn.cursor()