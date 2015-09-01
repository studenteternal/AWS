#!/usr/bin/python

import yaml
import boto


print "import worked"

#serverlist = open ("aws-server-list",'a')

s3 = boto.connect_s3()
bucket = s3.create_bucket('media.studenteternal.net')
key = bucket.new_key('examples/first_file.csv')
key.set_contents_from_filename('/home/jeff/first_file.csv')
key.set_acl('public-read')


#serverlist.close()

