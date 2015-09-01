#!/usr/bin/python

import yaml
import boto


print "import worked"

#serverlist = open ("aws-server-list",'a')

ec2 = boto.connect_ec2()
reservation = ec2.run_instances (image_id='ami-bb709dd2', key_name='aws-studenteternal')

#wait for the instance to boot
for r in ec2.get_all_instances():
	if r.id == reservation.id:
		break
print r.instances[0].public_dns_name 


#serverlist.close()

