#!/usr/bin/env python3
from ceilometer import getCeilometer
from nova import getNova

def createAlarmID():
	NovaID = []
	alarmList = []
	for server in getNova().servers.list(search_opts={'all_tenants': 1}):
	    NovaID.append(server.id) #Gets the server ID number
	if getCeilometer().alarms.list() == []:
		for server in NovaID:
	       		alarmdictCPU = {'name':'1%s'%server, 'description':'cpu theshold', 'meter_name':'cpu_util', 'threshold':'30', 
	       			'comparison_operator':'gt', 'period':'15', 'evaluation_periods':'1', 'alarm_action': 'log://',  
	       				'q':'resource_id =%s'%server}

	       		alarmdictIncomingBytes = {'name':'2%s'%server, 'description':'node incoming bytes', 
	       			'meter_name':'network.incoming.bytes', 'threshold':'110', 'comparison_operator':'gt', 'period':'15', 
	       				'evaluation_periods':'1', 'alarm_action': 'log://',  'q':'resource_id =%s'%server}
			alarmdictIncomingBytesRate = {'name':'3%s'%server, 'description':'node incoming bytes rate',
                                'meter_name':'network.incoming.bytes.rate', 'threshold':'110', 'comparison_operator':'gt', 'period':'15',
                                        'evaluation_periods':'1', 'alarm_action': 'log://',  'q':'resource_id =%s'%server}

	       		getCeilometer().alarms.create(aodh_enabled=True,**alarmdictCPU)

	    		getCeilometer().alarms.create(aodh_enabled=True,**alarmdictIncomingBytes)
			
			getCeilometer().alarms.create(aodh_enabled=True,**alarmdictIncomingBytesRate)
			
	alarmlist = getCeilometer().alarms.list()
	for list in alarmlist:
	   	alarmList.append(list.alarm_id) 
	return alarmList
