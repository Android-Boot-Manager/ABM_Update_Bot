import logging
from json import dumps

from certifi import where as cert_where
from urllib3 import PoolManager

from ..utils.lambda_configuration import LambdaConfiguration


class Telegram:
    TELEGRAM_TOKEN: str = ""
    HTTP_CLIENT: PoolManager = PoolManager(ca_certs=cert_where())
    API_URL_TEMPLATE: str = "https://api.telegram.org/bot{token}/{method}"
    LAMBDA_CONF: LambdaConfiguration = LambdaConfiguration()
    LOG: logging.Logger = logging.getLogger("telegram")

    def __init__(self):
        self.TELEGRAM_TOKEN = self.LAMBDA_CONF.get_telegram_token()

    def __method_url(self, method: str) -> str:
        return self.API_URL_TEMPLATE.format(token=self.TELEGRAM_TOKEN, method=method)

    def __send_payload(self, url: str, body: dict) -> None:
        self.HTTP_CLIENT.request(
            "POST", url, body=dumps(body), headers={"Content-Type": "application/json"}
        )

    def send_message(self, channel: str, text: str) -> None:
        self.__send_payload(
            self.__method_url("sendMessage"),
            {
                "chat_id": channel,
                "text": text,
            },
        )
