#!/usr/bin/env python3

import boto3
import sys

#usage create-instance.py AWS-REGION

region = sys.argv[1]
ec2 = boto3.client('ec2', region_name=(region))
instances = ec2.run_instances(
	ImageId='ami-8c122be9', 
	KeyName=(region)+'-charming',
	MinCount=1, 
	MaxCount=1,
	InstanceType="t2.micro",
	SecurityGroups=[(region)+'-charming',],
	)	
	
