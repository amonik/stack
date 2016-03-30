#!/usr/bin/env python


#make this a class
import keystoneclient.v2_0.client as k_client
#from constants import *
import ceilometerclient.v2 as c_client
import os
from novaclient.v2 import client
import novainstance

CEILOMETER_URL='http://localhost:8777'
try:
    def get_keystone_creds():
    	#define dictionary
        d = {}
        d['username'] = os.environ['OS_USERNAME']
        d['password'] = os.environ['OS_PASSWORD']
        d['auth_url'] = os.environ['OS_AUTH_URL']
        d['tenant_name'] = os.environ['OS_TENANT_NAME']
        return d
except (KeyError,RuntimeError, TypeError, NameError):
    print "Please import your RC file"
    
creds = get_keystone_creds()

keystone = k_client.Client(**creds)

auth_token = keystone.auth_token
ceilometer = c_client.Client(endpoint=CEILOMETER_URL, token= lambda : auth_token )

#meterlist = ceilometer.meters.list()
#novainstance.get_nova_creds()
for server in getInstanceID():
    query = [dict(field ='resource_id', op ='eq', value = server)]
    cpu_util_sample = ceilometer.samples.list(meter_name = 'cpu_util', q = query,limit = 1)
    for each in cpu_util_sample:
        print each.timestamp, each.resource_id, each.counter_volume








'''
#Get ID number of each Nova instance. store each instance in array. 	
nova list

get ID, Name, and Networks

#Get the meters that you want to monitor

pull these meters every 2 min. Make sure to change /etc/ceilometer/pipeline.yaml file to allow the meters to refresh every min.

#Check to meter for each Nova instance and the Threshold
create a Class that has all thresholds in Functions. Call the functions in main file.
#If it goes over that threshold pause the instance
nova pause NAME
nova delete name
'''