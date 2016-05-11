#!/usr/bin/env python

from credentials import heat_port
import keystoneclient.v2_0.client as ksclient
from credentials import get_keystone_creds
from heatclient.client import Client

def getHeat():
	creds = get_keystone_creds()
   	keystone = ksclient.Client(**creds)
	token = keystone.auth_token
	auth_token = token
	heat = Client('1', endpoint=heat_port(), token=auth_token)
	return heat
	
