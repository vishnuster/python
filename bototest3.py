import boto3
session=boto3.Session(profile_name='default')
s3=session.client('s3')
s3.create_bucket(Bucket='vishnu1243asdash')
s3.create_bucket(Bucket='vishnu1243asdh')
for res in s3.list_buckets():
    a=res.name
    resp=s3.delete_bucket(Bucket='a')
    print(resp)








