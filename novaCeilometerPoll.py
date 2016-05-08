#!/usr/bin/env python

__author__ = "Adeyin Amon Ikpah-Aziaruh"
__version__ = "2.0"

from ceilometer import getCeilometer
from nova import getNova
import time
from ceilometerAlarms import createAlarmID
now = time.strftime("%c")

if __name__ == '__main__':
    meterName = []
    Node = []
    createAlarmID()
    for alarmID in createAlarmID():
	if getCeilometer().alarms.get_state(alarmID) == 'alarm':
		Node.append(getCeilometer().alarms.get(alarmID).name[1:])
		meterName.append(getCeilometer().alarms.get(alarmID).threshold_rule.get('meter_name'))
    for item in meterName:
	print item
    for item in Node:
	print item
    NovaID = []
    for server in getNova().servers.list(search_opts={'all_tenants': 1}):
        NovaID.append(server.id) #Gets the server ID number

    for server in NovaID:
        query = [dict(field ='resource_id', op ='eq', value = server)] #gets resource ID from server

        query2 = [{'field': 'metadata.instance_id', 'op': 'eq', 'value': server}] #gets instance ID from metadata

        cpu_util_sample = getCeilometer().samples.list(meter_name = 'cpu_util',q=query, limit = 1)

        network_outgoing_bytes_rate_sample = getCeilometer().samples.list(meter_name = 'network.outgoing.bytes.rate', q = query2, limit = 1 ) 
	
	network_incoming_bytes_rate = getCeilometer().samples.list(meter_name = 'network.incoming.bytes.rate', q = query2, limit = 1)

        getServerNameFromServerID = getNova().servers.get(server)
        getServerNameFromServerID.name
        

        for each in cpu_util_sample:
            getServerNameFromServerID = getNova().servers.get(server)
            print("The cpu util of %s: " % getServerNameFromServerID.name)
            print each.counter_volume

        for each in network_outgoing_bytes_rate_sample:
            print("The outgoing bytes rate of server %s:" % getServerNameFromServerID.name)
            print each.counter_volume 
	
	for each in network_incoming_bytes_rate:
	    print("The incoming bytes rate of server %s:" % getServerNameFromServerID.name)
	    print each.counter_volume
        print(now)
    
