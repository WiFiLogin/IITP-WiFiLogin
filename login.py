#!/usr/bin/env python
#Copyright Muks 2016-2020, muks14x@gmail.com
import os,time,mechanize
username = 'biswas.cs16';
password = 'ip';
def signin():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open('http://10.120.120.22:8090/httpclient.html')
    br.form = list(br.forms())[0]
    br.form['username'] = username
    br.form['password'] = password
    br.submit()
signin()

if os.system('ping -c 1 8.8.8.8')==0:
    print'Successfully logged In!'
else:
	print 'Error'