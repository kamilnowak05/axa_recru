from typing import Dict

from loguru import logger

from app.clients.base_client import BaseHttpClient, Methods
from env import Env


class Endpoints:
    trade = "/split"


class _ControllerServerClient(BaseHttpClient):
    def __init__(self) -> None:
        super().__init__(Env.CONTROLLER_SERVER_URL)

    async def send_splits(self, data: Dict[str, int]) -> None:
        logger.debug("Sending splits to controller server...")
        error_msg = "Could not send request to controller server"
        path = Endpoints.trade
        await self._request(Methods.POST, error_msg, path, json=data)


ControllerServerClient = _ControllerServerClient()
