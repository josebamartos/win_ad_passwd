#!/usr/bin/env python

import ldap

address  = ''    # Remote Windows host hostname or IP address
username = ''    # Format: CN=Name,CN=Users,CN=domain,CN=com
password = ''    # Remote Windows host password

conn = ldap.initialize("ldap://" + address)
conn.protocol_version = 3
conn.set_option(ldap.OPT_REFERRALS, 0)

try:
    result = conn.simple_bind_s(username, password)
except ldap.INVALID_CREDENTIALS:
    print "Invalid credentials"
    exit(1)
except ldap.SERVER_DOWN:
    print "Server down"
    exit(1)
except ldap.LDAPError, e:
    if type(e.message) == dict and e.message.has_key('desc'):
        print "Other LDAP error: " + e.message['desc']
        exit(1)
    else: 
        print "Other LDAP error: " + e
        exit(1)
finally:
    conn.unbind_s()

print "Succesfully authenticated"
