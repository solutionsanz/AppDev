# myOracleDBConn1.py

from __future__ import print_function

import os
import sys
import cx_Oracle

dbusername = sys.argv[1];
dbpassword = sys.argv[2];
dbservicename = sys.argv[3];

connection = cx_Oracle.connect(dbusername, dbpassword, dbservicename)

cursor = connection.cursor()
cursor.execute("""
    SELECT table_name
    FROM user_tables 
    ORDER BY table_name"""
    )
for tablename in cursor:
    print("Values:", tablename)
