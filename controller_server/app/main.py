import asyncio
from typing import Dict, List

from fastapi import FastAPI, HTTPException, status, Depends

from app.clients.position_server_client import PositionServerClient
from app.jwt import decode_jwt
from app.models import Account, Trade

app = FastAPI()

TRADES: List[Trade] = []


async def send_positions(accounts: List[Account]) -> None:
    async with asyncio.Lock():
        global TRADES
        trades = TRADES
        TRADES = []

    stock_trades: Dict[str, int] = {}
    for trade in trades:
        if stock_trades.get(trade.stock_ticker.value):
            stock_trades[trade.stock_ticker.value] += trade.quantity
        else:
            stock_trades[trade.stock_ticker.value] = trade.quantity

    positions = {
        account.name: "".join(
            f"{account.value / value} {stock}, "
            for stock, value in stock_trades.items()
            if value
        )
        for account in accounts
    }

    await PositionServerClient.send_positions(positions)


@app.post("/trade", dependencies=[Depends(decode_jwt)], status_code=status.HTTP_200_OK)
async def fill_trade(data: Trade) -> None:
    TRADES.append(data)


@app.post("/split", dependencies=[Depends(decode_jwt)], status_code=status.HTTP_200_OK)
async def split_to_accounts(data: Dict[str, int]) -> None:
    accounts: List[Account] = []
    for name, value in data.items():
        accounts.append(Account(name=name, value=value))

    if sum(account.value for account in accounts) != 100:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Sum of percentages of all accounts should be equal to 100",
        )

    await send_positions(accounts)
