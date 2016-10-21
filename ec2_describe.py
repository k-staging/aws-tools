#!/bin/env python
# coding: utf-8
import sys
import boto3
from boto3.session import Session

def ec2_describe(profile, keyword):
    session = boto3.session.Session(profile_name=profile)
<<<<<<< HEAD
    client = session.client('ec2')
    paginator = client.get_paginator('describe_instances')
    page_iterator = paginator.paginate(
        Filters=[
            {
                'Name': 'tag-value',
                'Values': [
                    "*" + keyword + "*",
                ]
            }
        ]
    )
    for page in page_iterator:
        for ec2_list in page['Reservations']:
            for ec2 in ec2_list['Instances']:
                for nametag in ec2['Tags']:
                    if nametag['Key'] == 'Name':
                        instance_nametag = nametag['Value']
                instance_id = ec2['InstanceId']
                public_dns = ec2['PublicDnsName']
                private_ip = ec2['PrivateIpAddress']
                instance_type = ec2['InstanceType']
                instance_launchtime = ec2['LaunchTime']
                print '{0: <40}{1: <15}{2: <15}{3: <60}{4: <20}{5}'.format( instance_nametag, instance_id, instance_type, public_dns, private_ip, instance_launchtime )
=======
    ec2_list = session.client('ec2')
    ec2_list = ec2_list.describe_instances()
    ec2_list = ec2_list['Reservations']
    for ec2 in ec2_list:
        instance_nametag = ec2['Instances'][0]['Tags'][0]['Value']
        instance_id = ec2['Instances'][0]['InstanceId']
        public_dns = ec2['Instances'][0]['PublicDnsName']
        private_ip = ec2['Instances'][0]['PrivateIpAddress']
        instance_type = ec2['Instances'][0]['InstanceType']
        instance_launchtime = ec2['Instances'][0]['LaunchTime']
        print '{0: <25}{1: <15}{2: <15}{3: <60}{4: <15}{5}'.format( instance_nametag, instance_id, instance_type, public_dns, private_ip, instance_launchtime )
>>>>>>> parent of 7446913... ec2_describe.pyのnametag修正

if __name__ == '__main__':
    keyword = ''
    argvs = sys.argv
    argc = len(argvs)
    if argc != 2 and argc != 3:
        print 'python ec2_describe.py [profile_name] {keyword]'
        quit()
    if argc == 3:
        keyword = argvs[2]

    profile = argvs[1]
    ec2_describe(profile, keyword)
