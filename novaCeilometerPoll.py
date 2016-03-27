#!/usr/bin/env python

import keystoneclient.v2_0.client as k_client
import ceilometerclient.v2 as c_client
from novaclient.v2 import client
import os
#import threshold

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d
    try:
        get_nova_creds()
        pass
    except (KeyError,RuntimeError, TypeError, NameError):
        print "\nPlease import your RC file."

def get_keystone_creds():
    #define dictionary
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d
    try:
        get_keystone_creds()
        pass
    except (KeyError,RuntimeError, TypeError, NameError):
        print "\nPlease import your RC file."

def getNova():
    
    VERSION = '2'
    creds = get_nova_creds()
    nova = client.client.Client(VERSION,**creds)
    return nova

def getCeilometer():

    CEILOMETER_URL='http://localhost:8777'
    creds = get_keystone_creds()
    keystone = k_client.Client(**creds)
    auth_token = keystone.auth_token
    ceilometer = c_client.Client(endpoint=CEILOMETER_URL, token= lambda : auth_token )
    return ceilometer
   
if __name__ == '__main__':
    
    NovaID = []
    for server in getNova().servers.list(search_opts={'all_tenants': 1}):
        NovaID.append(server.id) 

    for server in NovaID:
        query = [dict(field ='resource_id', op ='eq', value = server)]
        cpu_util_sample = getCeilometer().samples.list(meter_name = 'cpu_util', q = query,limit = 1)
        for each in cpu_util_sample:
            print each.timestamp, each.resource_id, each.counter_volume