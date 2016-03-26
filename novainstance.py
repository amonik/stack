import os
from novaclient.v2 import client
try:
    def get_nova_creds():
        d = {}
        d['username'] = os.environ['OS_USERNAME']
        d['api_key'] = os.environ['OS_PASSWORD']
        d['auth_url'] = os.environ['OS_AUTH_URL']
        d['project_id'] = os.environ['OS_TENANT_NAME']
        return d
except (KeyError,RuntimeError, TypeError, NameError):
    print "Please import your RC file"


def getInstanceID():
    ID = []
    VERSION = '2'
    creds = get_nova_creds()
    nova = client.client.Client(VERSION,**creds)

    for server in nova.servers.list(search_opts={'all_tenants': 1}):
        ID.append(server.id) #, server.name
    return ID