#!/usr/bin/env python

from novaclient import client as novaclient
from credentials import get_nova_creds

def getNova():
	creds = get_nova_creds()
	nova = novaclient.Client("2", **creds)
	return nova


