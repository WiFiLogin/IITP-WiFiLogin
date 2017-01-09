#!/usr/bin/env python
#Copyright Mukuntha N S(muks14x) 2016-2020, muks14x@gmail.com
import os,time,mechanize,pickle

config = '.wifilogin.pickle'

if(not os.path.isfile(config)):
    username = raw_input('Enter Username:');
    password = raw_input('Enter Password:');
    with open(config, 'w') as f:
        pickle.dump([username,password], f)

with open(config) as f:
    username, password = pickle.load(f)

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
