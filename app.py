#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from aws_cdk import core
from cdk_modules.vpc import VPCStack
from cdk_modules.s3 import S3Stack

app = core.App()
vpc_stack = VPCStack(app, "VPCStack")
s3_stack = S3Stack(app, "S3Stack")

app.synth()
