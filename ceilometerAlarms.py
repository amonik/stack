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
	       		alarmdictCPU = {'name':'cpu high%s'%server, 'description':'cpu theshold', 'meter_name':'cpu_util', 'threshold':'30', 
	       			'comparison_operator':'gt', 'period':'15', 'evaluation_periods':'1', 'alarm_action': 'log://',  
	       				'q':'resource_id =%s'%server}

	       		alarmdictIncomingBytes = {'name':'incoming bytes%s'%server, 'description':'node incoming bytes', 
	       			'meter_name':'network.incoming.bytes', 'threshold':'180', 'comparison_operator':'gt', 'period':'15', 
	       				'evaluation_periods':'1', 'alarm_action': 'log://',  'q':'resource_id =%s'%server}

	       		getCeilometer().alarms.create(aodh_enabled=True,**alarmdictCPU)

	    		getCeilometer().alarms.create(aodh_enabled=True,**alarmdictIncomingBytes)
	alarmlist = getCeilometer().alarms.list()
	for list in alarmlist:
	   	alarmList.append(list.alarm_id) 
	return alarmList
