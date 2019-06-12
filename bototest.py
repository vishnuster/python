import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId = '1ami-0080e4c5bc078760e',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'cloudformationtest')
print (instance[0].id)