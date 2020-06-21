#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:41:50 2018

@author: wayne
"""

import pymysql.cursors
import smtplib
import os
import sys
from email.mime.text import MIMEText

db = pymysql.connect(host="",    # your host, usually localhost
                     user="",         # your username
                     passwd="",           # your password
                     db="")        # name of the data base
cur = db.cursor()

# you must create a Cursor object. It will let you execute all the queries you need.
cur = db.cursor()

#prepare SQL query for INSERT
cur.execute("select mxtemp,mntemp from history order by dt desc limit 1;")
result = "max: %s min: %s" % cur.fetchone()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("", "")

msg = MIMEText(result)
#close cursor
cur.close()

#close connection
db.close()

msg['Subject'] = ''
msg['From'] = ''
msg['To'] = ''

server.sendmail('', '', msg.as_string())
server.quit()
