AWSTemplateFormatVersion: 2010-09-09
Mappings:
  RegionMaps:
    us-east-1:
      AMI: ami-0080e4c5bc078760e
    ap-southeast-2:
      AMI: ami-43874721

Resources:
  Myinstance:
    Type: 'AWS::EC2::Instance'
    Properties:
      ImageId: !FindInMap
        - RegionMaps
        - !Ref 'AWS::Region'
        - AMI
      Tags:
        - Key: 'Name'
          Value: !Join
            - " "
            - - 'cloudformation-test-instance'
              - !Ref 'AWS::Region'
      SecurityGroups:
        - !Ref Mysecuritygroup
  Mysecuritygroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupName: test-sg
      GroupDescription: Incoming traffic on port 22 from 182.76.82.167
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 182.76.82.166/32