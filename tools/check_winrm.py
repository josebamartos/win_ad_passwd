#!/usr/bin/env python

import winrm

address  = ''    # Remote Windows host hostname or IP address
username = ''    # Remote Windows host username
password = ''    # Remote Windows host password

s = winrm.Session(address, auth=(username, password))
r = s.run_cmd('ipconfig', ['/all'])
   
print
print "======================================"
print "==== Remote WinRM service checker ===="
print "======================================"
print
print "==== Command status ===="
print "Status code: " + str(r.status_code)
print
print "==== Standard output ===="
print r.std_out
print
print "==== Standard error ===="
print r.std_err
print
