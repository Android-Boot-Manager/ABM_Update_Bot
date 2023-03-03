import json
import base64
import hashlib
import hmac
import os

from utils.lambda_configuration import LambdaConfiguration


def lambda_handler(event, context) -> dict:
    # Init LambdaConfiguration
    lambda_conf = LambdaConfiguration()

    target_gh_secret = lambda_conf.get_github_webhook_secret()
    receiv_gh_secret = ""

    return {
        "statusCode": 200,
    }
