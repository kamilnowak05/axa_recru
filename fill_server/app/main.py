from asyncio import sleep
from decimal import Decimal
from random import randrange

from fastapi import FastAPI

from app.clients.fill_server_client import ControllerServerClient
from app.models import StockTickerEnum, Trade

app = FastAPI()


async def send_trade() -> None:
    while True:
        await ControllerServerClient.send_trades(
            Trade(
                stock_ticker=StockTickerEnum.axa,
                price=Decimal.from_float(randrange(0, 10000)),
                quantity=randrange(0, 100),
            )
        )
        await sleep(randrange(1, 10))


@app.on_event("startup")
async def on_startup() -> None:
    await send_trade()
