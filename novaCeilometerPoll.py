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


def max_cpu_util():
    cpu_util = 30
    return cpu_util

def max_network_outgoing_bytes_rate():
    network_outgoing_bytes_rate = 100
    return network_outgoing_bytes_rate

def max_memory_usage():
    memory_usage = 80
    return memory_usage
   
if __name__ == '__main__':
    
    NovaID = []
    for server in getNova().servers.list(search_opts={'all_tenants': 1}):
        NovaID.append(server.id) 

    for server in NovaID:
        query = [dict(field ='resource_id', op ='eq', value = server)]

        query2 = [{'field': 'metadata.instance_id', 'op': 'eq', 'value': server}]

        cpu_util_sample = getCeilometer().samples.list(meter_name = 'cpu_util',q=query, limit = 1)

        network_outgoing_bytes_rate_sample = getCeilometer().samples.list(meter_name = 'network.outgoing.bytes.rate', q = query2, limit = 1 ) 

        getServerNameFromServerID = getNova().servers.get(server)
        getServerNameFromServerID.name
        

        for each in cpu_util_sample:
            getServerNameFromServerID = getNova().servers.get(server)
            print("The cpu_util of %s: " % getServerNameFromServerID.name)
            print each.counter_volume
            if each.counter_volume >= max_cpu_util():
                print("deleting server %s becasue cpu_util is greater than %s" % (getServerNameFromServerID.name,max_cpu_util()))
                getNova().delete(each.resource_id) #will delete resource.
                print("server %s deleted" % getServerNameFromServerID.name)

        for each in network_outgoing_bytes_rate_sample:
            print("The network_outgoing_bytes_rate of server %s:" % getServerNameFromServerID.name)
            print each.counter_volume  

    
