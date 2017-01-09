#!/bin/bash
#Copyright 2016 Mukuntha, tameeshb http://tameesh.in/muks
python login.py;
ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && notify-send  'IIT P Wifi' 'Successfully Logged in!' -i /home/tameeshb/terminal.ico || notify-send 'IIT P WiFi' 'Error!' -i /home/tameeshb/terminal.ico;
