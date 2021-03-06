#!/usr/bin/env python
import os

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = OS_AUTH_URL= 'http://localhost:5000/v2.0/'
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

def heat_port():
   
    d  = 'http://localhost:8004/v1.0/%s' % os.environ['OS_TENANT_ID']

    return d
