from aws_cdk import (
    aws_ec2 as ec2,
    core as cdk
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class VPCStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(self, 'devVPC',
                           cidr="10.0.0.0/16",
                           max_azs=1,
                           enable_dns_support=True,
                           enable_dns_hostnames=True,
                           subnet_configuration=[
                               ec2.SubnetConfiguration(
                                   name="Public",
                                   subnet_type=ec2.SubnetType.PUBLIC,
                                   cidr_mask=24
                               ),
                               ec2.SubnetConfiguration(
                                   name="Private",
                                   subnet_type=ec2.SubnetType.PRIVATE,
                                   cidr_mask=24
                               )
                           ],
                           nat_gateways=1
                           )

        priv_sub_id = [subnets.subnet_id for subnets in self.vpc.private_subnets]
