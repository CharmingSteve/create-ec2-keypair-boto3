#!/usr/bin/env python3

# usage ./create-security-group.py AWS-REGION
# this creates a sec group in the region you chose called AWS-REGION-charming and opens ports 22 for ssh and 80 for http

import boto3
import sys

region = sys.argv[1]

ec2 = boto3.client('ec2', region_name=(region))

# Create sec group
sec_group = ec2.create_security_group(GroupName=(region)+'-charming', Description='CharmingWebServer')


ec2.authorize_security_group_ingress(GroupName=(region)+'-charming' ,IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=22,ToPort=22)

ec2.authorize_security_group_ingress(GroupName=(region)+'-charming' ,IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=80,ToPort=80)


