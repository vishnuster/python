#Deleting all the buckets from an account
import boto3
s3=boto3.resource('s3')
for i in s3.buckets.all():
    print("Iam going to delete all these buckets:", i)
    i.delete()
    print(i,"deleted")


