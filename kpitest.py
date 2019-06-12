 This template creates the Data Lake dynamo tables and elasticsearch
# domains.  It must be run in both regions prior to running the "main"
# template.
#
# Once this stack is created in both regions there is additional manual config:
# 1. Convert each table into a Global Table and ensure capacity auto scaling
#    is enabled.
# 2. Update the Elasticsearch clusters to provision "enough".
# 3. Configure the access policy for each ES domain.  This must be done after
#    the main template is complete, b/c we need the Lambda role arn that it
#    creates.
# An example elasticsearch policy:
#  {
#    "Version": "2012-10-17",
#    "Statement": [
#    {
#      "Effect": "Allow",
#      "Principal": {
#        "AWS": "arn:aws:iam::421292395054:role/colin-test-lake-LambdaExecutionRole-FC6RN1Q0S3SW"
#      },
#      "Action": "es:*",
#      "Resource": "arn:aws:es:us-east-1:421292395054:domain/datalake-colin2-content/*"
#    }
#    ]
#  }
#
# The "AWS" property is the lambda execution role created by the 'main'
# template.  It is output in cfn as LambdaExecutionRole, so you can copy the
# value from there.

Parameters:
  Stage:
    Type: String
    Description: Name of the stage to deploy (prd, stage, etc.)  #Parameter is provided in jenkins gui


Mappings:
  # datalk-nonprod mappings
  "815622608052":
    us-east-1:
      ElasticsearchKmsKeyId: 1d66636f-1a1b-4cf6-a2e3-55bcad8ebedb
    us-west-2:
      ElasticsearchKmsKeyId: f879e798-89d4-4994-8f66-911c89c51771

  # CD-prod mappings
  "055860007327":
    us-east-1:
      ElasticsearchKmsKeyId: 03ed5d70-2a00-4ad5-821d-d15b9671c539
    us-west-2:
      ElasticsearchKmsKeyId: 26bdc198-96a9-4747-a99e-be5cf43c4bd9


Conditions:
  EncryptEs: !Equals [ !Ref Stage, prod ]   # EncryptEs is used in multiple places below. This means if Stage = prod only then execute the properties below where EncryptEs is specified


Resources:              #Dynamo db tables datalake-${Stage}-creds, datalake-${Stage}-file, datalake-${Stage}-pending-files
  # Dynamo tables
  CredsTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub "datalake-${Stage}-creds"
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 2
        WriteCapacityUnits: 8
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES  # "new and old" stream required for Global Table
      SSESpecification:
        SSEEnabled: true

  FilesTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub "datalake-${Stage}-files"
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 2
        WriteCapacityUnits: 8
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      SSESpecification:
        SSEEnabled: true

  PendingFilesTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub "" \
                      ""
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 2
        WriteCapacityUnits: 8
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      SSESpecification:
        SSEEnabled: true

  RolesTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub "datalake-${Stage}-roles"
      AttributeDefinitions:
        - AttributeName: rolename
          AttributeType: S
      KeySchema:
        - AttributeName: rolename
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 2
        WriteCapacityUnits: 8
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      SSESpecification:
        SSEEnabled: true

  BulkFilesListTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub "datalake-${Stage}-bulkfileslist"
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: "S"
        - AttributeName: "sequence-number"
          AttributeType: "S"
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 2
        WriteCapacityUnits: 8
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      SSESpecification:
        SSEEnabled: true
      GlobalSecondaryIndexes:
      -
        IndexName: "sequence-number-index"
        KeySchema:
        -
          AttributeName: "sequence-number"
          KeyType: "HASH"
        Projection:
          ProjectionType: "ALL"
        ProvisionedThroughput:
          ReadCapacityUnits: 2
          WriteCapacityUnits: 8

  SchemaTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub "datalake-${Stage}-schema"
      AttributeDefinitions:
        - AttributeName: "name"
          AttributeType: "S"
        - AttributeName: "application-name"
          AttributeType: "S"
        - AttributeName: "business-unit"
          AttributeType: "S"
      KeySchema:
        - AttributeName: "name"
          KeyType: "HASH"
      ProvisionedThroughput:
        ReadCapacityUnits: 2
        WriteCapacityUnits: 8
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      SSESpecification:
        SSEEnabled: true
      GlobalSecondaryIndexes:
      -
        IndexName: "application-name-index"
        KeySchema:
        -
          AttributeName: "application-name"
          KeyType: "HASH"
        Projection:
          ProjectionType: "ALL"
        ProvisionedThroughput:
          ReadCapacityUnits: 2
          WriteCapacityUnits: 8
      -
        IndexName: "business-unit-index"
        KeySchema:
        -
          AttributeName: "business-unit"
          KeyType: "HASH"
        Projection:
          ProjectionType: "ALL"
        ProvisionedThroughput:
          ReadCapacityUnits: 2
          WriteCapacityUnits: 8

  # Elasticsearch domains
  EsMetadataDomain:
    Type: AWS::Elasticsearch::Domain
    DeletionPolicy : Delete
    Properties:
      DomainName: !Sub "datalake-${Stage}-metadata"
      ElasticsearchVersion: "5.5"
      ElasticsearchClusterConfig:
        DedicatedMasterEnabled: "false"
        InstanceCount: 1
        ZoneAwarenessEnabled: "false"
        InstanceType: !If [ EncryptEs, m4.large.elasticsearch, t2.medium.elasticsearch ]
      EBSOptions:
        EBSEnabled: true
        Iops: 0
        VolumeSize: 10
        VolumeType: "gp2"
      SnapshotOptions:
        AutomatedSnapshotStartHour: "0"
      EncryptionAtRestOptions:
        !If
          - EncryptEs
          -
            Enabled: true
            KmsKeyId: !FindInMap [ !Ref "AWS::AccountId", !Ref "AWS::Region", ElasticsearchKmsKeyId ]
          - !Ref "AWS::NoValue"
      AdvancedOptions:
        rest.action.multi.allow_explicit_index: "true"

  EsContentDomain:
    Type: "AWS::Elasticsearch::Domain"
    DeletionPolicy : "Retain"
    Properties:
      DomainName: !Sub "datalake-${Stage}-content"
      ElasticsearchVersion: "5.5"
      ElasticsearchClusterConfig:
        DedicatedMasterEnabled: "false"
        InstanceCount: 1
        ZoneAwarenessEnabled: "false"
        InstanceType: !If [ EncryptEs, m4.large.elasticsearch, t2.medium.elasticsearch ]
      EBSOptions:
        EBSEnabled: true
        Iops: 0
        VolumeSize: 10
        VolumeType: "gp2"
      SnapshotOptions:
        AutomatedSnapshotStartHour: "0"
      EncryptionAtRestOptions:
        !If
          - EncryptEs
          -
            Enabled: true
            KmsKeyId: !FindInMap [ !Ref "AWS::AccountId", !Ref "AWS::Region", ElasticsearchKmsKeyId ]
          - !Ref "AWS::NoValue"
      AdvancedOptions:
        rest.action.multi.allow_explicit_index: "true"

  # The file notification SNS topic
  FileNotificationTopic:
    Type: 'AWS::SNS::Topic'
    Properties:
      TopicName: !Sub "datalake-${Stage}-file-notify"

  # queue to hold s3 'object created' events
  FileArrivalQueue:
    Type: AWS::SQS::Queue
    Properties:
      VisibilityTimeout: 30   # seconds (must be longer than filearrival lambda timeout)
      MessageRetentionPeriod: 259200  # 3 days (should be less than DLQ)
      RedrivePolicy:
        deadLetterTargetArn: !GetAtt FileArrivalDLQ.Arn
        maxReceiveCount: 20

  # allows the S3 file bucket to send new file notifications to the queue
  FileArrivalQueuePolicy:
    Type: AWS::SQS::QueuePolicy
    Properties:
      PolicyDocument:
        Fn::Sub:
          - |
            {
              "Version": "2012-10-17",
              "Id": "allow-s3-publish-policy",
              "Statement": [
              {
                "Sid": "Sid1542137247654",
                "Effect": "Allow",
                "Principal": {
                  "AWS": "*"
                },
                "Action": "SQS:SendMessage",
                "Resource": "${QueueArn}",
                "Condition": {
                  "StringEquals": {
                    "aws:SourceArn": "arn:aws:s3:::datalake-${Stage}-files-${AWS::Region}"
                  }
                }
              }
              ]
            }
          - { QueueArn: !GetAtt FileArrivalQueue.Arn }

      Queues:
        - !Ref FileArrivalQueue

  FileArrivalDLQ:
    Type: AWS::SQS::Queue
    Properties:
      MessageRetentionPeriod: 604800  # 1 week in seconds

Outputs:
  FilesTableStream:
    Description: Dynamo files table stream arn
    Value: !Sub "${FilesTable.StreamArn}"
    Export:
      Name: !Sub "datalake-${Stage}-files-table-stream"

  EsMetadataDomain:
    Description: Endpoint for ES metadata domain
    Value: !GetAtt EsMetadataDomain.DomainEndpoint
    Export:
      Name: !Sub "datalake-${Stage}-es-metadata-endpoint"

  EsContentDomain:
    Description: Endpoint for ES content domain
    Value: !GetAtt EsContentDomain.DomainEndpoint
    Export:
      Name: !Sub "datalake-${Stage}-es-content-endpoint"

  FileNotificationTopic:
    Description: SNS topic to publish file arrival notifications
    Value: !Ref FileNotificationTopic
    Export:
      Name: !Sub "datalake-${Stage}-file-notification-topic"

  FileArrivalQueue:
    Description: SQS queue to hold file created events from S3
    Value: !GetAtt FileArrivalQueue.Arn
    Export:
      Name: !Sub "datalake-${Stage}-file-created-queue"This is a test!!!!!!!!!!!!!!!!