from typing import Dict

from loguru import logger

from app.clients.base_client import BaseHttpClient, Methods
from env import Env


class Endpoints:
    trade = "/print"


class _PositionServerClient(BaseHttpClient):
    def __init__(self) -> None:
        super().__init__(Env.POSITION_SERVER_URL)

    async def send_positions(self, data: Dict) -> None:
        logger.debug("Sending positions to position server...")
        error_msg = "Could not send request to position server"
        path = Endpoints.trade
        await self._request(Methods.POST, error_msg, path, json=data)


PositionServerClient = _PositionServerClient()
