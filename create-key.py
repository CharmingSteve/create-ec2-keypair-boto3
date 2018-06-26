!/usr/bin/env python3

import boto3
outfile = open('TestKey.pem','w')
ec2 = boto3.client('ec2')
keypair = ec2.create_key_pair(KeyName='JundiNV11')
i = keypair['KeyMaterial']
outfile.write(i)
outfile.close()
