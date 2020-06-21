#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:41:50 2018

@author: wayne
"""

import pymysql.cursors
import pandas as pd
import matplotlib.pyplot as plt

start="2018-08-01"
end="2018-09-01"

conn = pymysql.connect(host="", user="", password="",\
db="")
cursor = conn.cursor()
cursor.execute('select mxtemp,mntemp,mxdew,mndew,dt from history where \
dt >= %s and dt <= %s order by dt desc', (start, end))
results = cursor.fetchall()

df = pd.DataFrame( [[dfd for dfd in rows] for rows in results] )
df.rename(columns={0: 'MaxTemp', 1: 'MinTemp', 2: 'MaxDew', 3: 'MinDew', \
4: 'Date'}, inplace=True);

#for rows in rows:
#    print(rows)

maxtmp = df.MaxTemp
mintmp = df.MinTemp
#maxdew = df.MaxDew
#mindew = df.MinDew
dt = df.Date
#print(maxtmp,dt)

plt.title('Temperature, Highs and Lows')
plt.plot(dt,maxtmp, 'r-')
plt.plot(dt,mintmp, 'b-')
#plt.plot(dt,maxdew, 'g.--')
#plt.plot(dt,mindew, 'y.--')
plt.grid(True)
plt.ylabel('Temperature \n(fahrenheit)')
#plt.xlabel('Date')
plt.legend()
plt.show()
