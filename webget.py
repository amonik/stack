#!/usr/bin/env python
import os
import time
def webGet(n,ip):
	for x in xrange(n):
		os.system('wget -O - http://%s'%ip)
		time.sleep(3)

