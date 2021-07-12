from aws_cdk import (
    aws_s3 as s3,
    core as cdk
)


class S3Stack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        account_id = cdk.Aws.ACCOUNT_ID

        s3_bucket = s3.Bucket(self, "s3-bucket",
                              access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
                              encryption=s3.BucketEncryption.S3_MANAGED,
                              bucket_name=account_id + '-' + 'deploy-packages',
                              block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                              removal_policy=cdk.RemovalPolicy.DESTROY
                              )
