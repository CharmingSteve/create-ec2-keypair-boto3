#!/usr/bin/env python3

import boto3
import sys
nameofkey = sys.argv[1]
outfile = open((nameofkey)+'.pem','w')
ec2 = boto3.client('ec2')
keypair = ec2.create_key_pair(KeyName=(nameofkey))
i = keypair['KeyMaterial']
outfile.write(i)
outfile.close()
