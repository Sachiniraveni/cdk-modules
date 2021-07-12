#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from aws_cdk import core

from cdk_modules.vpc import VPCStack


app = core.App()
VPCStack(app, "VPCStack")

app.synth()
