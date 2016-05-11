from credentials import get_keystone_creds
from neutronclient.v2_0 import client
def getNeutron():
	neutron = client.Client(**get_keystone_creds())
	return neutron

