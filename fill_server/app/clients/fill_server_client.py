from loguru import logger

from app.clients.base_client import BaseHttpClient, Methods
from app.models import Trade
from Env import Env


class Endpoints:
    trade = "/trade"


class _ControllerClient(BaseHttpClient):
    def __init__(self) -> None:
        super().__init__(Env.CONTROLLER_SERVER_URL)

    async def send_trades(self, data: Trade) -> None:
        logger.debug("Sending trades to fill server...")
        error_msg = "Could not send request to fill server"
        path = Endpoints.trade
        await self._request(Methods.POST, error_msg, path, json=data.dict())


ControllerClient = _ControllerClient()
