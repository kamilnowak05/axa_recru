from asyncio import sleep
from decimal import Decimal
from random import randrange

from fastapi import FastAPI
from loguru import logger

from app.clients.controller_server_client import ControllerServerClient
from app.models import StockTickerEnum, Trade

app = FastAPI()


async def send_trade() -> None:
    for _ in range(50):
        for en in StockTickerEnum:
            trades = Trade(
                stock_ticker=en,
                price=Decimal.from_float(randrange(0, 10000)),
                quantity=randrange(0, 100),
            )
            await ControllerServerClient.send_trades(trades)
            logger.info(f"Trades: {trades.json()}")
            await sleep(randrange(1, 10))


@app.on_event("startup")
async def on_startup() -> None:
    await send_trade()
