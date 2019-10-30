# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='automatingTVA')
new_bucket = s3.create_bucket(Bucket='automatingTVA', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='automatingTVA', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
new_bucket = s3.create_bucket(Bucket='automatingPythonTVA', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
new_bucket = s3.create_bucket(Bucket='automatingPythonTVA', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='automatingpythontva', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='automatingpythontva', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
for bucket in s3.buckets.all():
    print(bucket)
    
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'awspython1')
get_ipython().run_line_magic('save', 'awspython1.py')
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'awspythontraining.py all')
get_ipython().run_line_magic('save', 'awspythontraining.py 1-50')
