Resources:
 Testinstance:
   Type: 'AWS::EC2::Instance'
   Properties:
     InstanceType: t2.micro
     ImageId: ami-0080e4c5bc078760e
     KeyName: cloudformationtest
     Tags:
       - Key: Name
         Value: testinstance
     SecurityGroups:
       - !Ref Testsg
     UserData:
       'Fn::Base64':
         |
           #!/bin/bash -xe
           useradd vishnu
           yum install -y httpd
           echo "<html>This is a test page.</html>" > /var/www/index.html
           service httpd start
 Testsg:
   Type: 'AWS::EC2::SecurityGroup'
   Properties:
     GroupDescription: open port 22 from for machine
     GroupName: testsg
     SecurityGroupIngress:
       - IpProtocol: tcp
         FromPort: 22
         ToPort: 22
         CidrIp: 182.76.82.166/32
Outputs:
  Instancedns:
    Description: Outputs the instance public DNS
    Value: !GetAtt Testinstance.PublicDnsName
  InstancepublicIp:
    Description: Outputs Public IP of instance
    Value: !GetAtt Testinstance.PublicIp
