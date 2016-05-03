#!/usr/bin/env python
from credentials import get_keystone_creds
from ceilometerclient.v2 import client as ceilo
def getCeilometer():

	CEILOMETER_URL='http://localhost:8777'
	creds = get_keystone_creds()
	ceilometer = ceilo.Client(endpoint=CEILOMETER_URL, **creds )
	return ceilometer
