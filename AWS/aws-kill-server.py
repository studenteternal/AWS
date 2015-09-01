#!/usr/bin/python

import yaml
import boto


print "import worked"

#serverlist = open ("aws-server-list",'a')

ec2 = boto.connect_ec2()

x = 0
#wait for the instance to boot
for r in ec2.get_all_instances():
	kill = ec2.stop_instances(instance_ids=[r.id]) 
	x = x + 1

print x 


#serverlist.close()

