from nova import getNova
import random
import paramiko
import time


def node():
	flavor = getNova().flavors.find(name="m1.tiny")
	name = "node%s"%random.randint(3,100000)
	image = getNova().images.find(name="cirros")
	nics = [{"net-id": getNova().networks.list()[0].id, "v4-fixed-ip": ''}]
	instance = getNova().servers.create(name, image, flavor, nics=nics)
	status = instance.status
	while status == 'BUILD':
	    time.sleep(5)
	    # Retrieve the instance again so the status field updates
	    instanceID = getNova().servers.get(instance.id)
	    status = instanceID.status
	print "status: %s" % status

	floating_ip = getNova().floating_ips.create()
	instance.add_floating_ip(floating_ip)

	username = "cirros"
	password = "cubswin:)"
	server = floating_ip.ip
	ssh = paramiko.SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	time.sleep(20)
	ssh.connect(server, username=username, password=password)
	time.sleep(30)
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("MYIP=$(ifconfig eth0|grep 'inet addr'|awk -F: '{print $2}'| awk '{print $1}')\nwhile true; do echo -e 'HTTP/1.0 200 OK\r\n\r\nWelcome to $MYIP' | sudo nc -l -p 80 ; done&")
	return instance

