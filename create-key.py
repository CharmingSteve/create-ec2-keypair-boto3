#!/usr/bin/env python3

import boto3
import sys
import urllib.request
import os
f = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/placement/availability-zone/')
region = (f.read(100).decode('utf-8')[:-1])
outfile = open((region)+'.pem','w')
ec2 = boto3.client('ec2', region_name=(region))
keypair = ec2.create_key_pair(KeyName=(region))
i = keypair['KeyMaterial']
outfile.write(i)
outfile.close()
os.chmod((region)+'.pem', 400)
