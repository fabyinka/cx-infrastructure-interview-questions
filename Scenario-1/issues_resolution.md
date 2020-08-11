Issues:
Template contains errors.: Template format error: Unresolved resource dependencies [pArtifactS3Key, pArtifactS3BucketName, pLogLevel] in the Resources block of the template.

Diagnosis:
The issue was that !Ref can only works for Logical ID that exists within the template.

resolution

Specified the relevant SSM parameters for pArtifactS3Key, pArtifactS3BucketName and pLogLevel as below. Another possible way to resolve this would have been to create a template that manages all the parameters and then use the Export/Import feature of CloudFormation to reference them between stacks.

Parameters:
  pArtifactS3Key:
    Default: ArtifactKey
    Description: Name of the Artifact S3 Key
    Type: AWS::S3::S3Artifact::pArtifactS3Key
  pArtifactS3BucketName:
    Description: Name of artifact bucketname
    Type: AWS::S3::S3BucketName::pArtifactS3BucketName
