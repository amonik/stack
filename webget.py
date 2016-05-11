#!/usr/bin/env python
import os
import time
from random import randint
def webGet(n,ip):
	for x in xrange(n):
		os.system('wget -O - http://%s'%ip)
		time.sleep(randint(1,6))

