from os import getenv
from typing import Optional


class LambdaConfiguration:
    def __init__(self):
        # This class doesn't initialise anything, but instead dynamically gets
        # relevant environmental variables from the Lambda function's run-time
        # envronment.
        pass

    @staticmethod
    def get_telegram_token() -> Optional[str]:
        try:
            return getenv("LAMBDA_FUNC_TELEGRAM_TOKEN")
        except KeyError:
            # Return None, as we can't get the env var
            return None

    @staticmethod
    def get_github_webhook_secret() -> Optional[str]:
        try:
            return getenv("LAMBDA_FUNC_GITHUB_WEBHOOK_SECRET")
        except KeyError:
            # Return None, as we can't get the env var
            return None

    @staticmethod
    def get_telegram_group_id() -> Optional[int]:
        try:
            return int(getenv("LAMBDA_FUNC_TELEGRAM_GROUP_ID"))
        except KeyError:
            # Return None, as we can't get the env var
            return None
