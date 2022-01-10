from asyncio import sleep
from random import randrange
from typing import Dict

from fastapi import FastAPI

from app.clients.controller_server_client import ControllerServerClient

app = FastAPI()


async def send_splits() -> None:
    for _ in range(25):
        accounts: Dict[str, int] = {}
        for account in range(randrange(0, 100)):
            value = randrange(100)
            if sum(accounts.values()) + value > 100:
                value = 100 - sum(accounts.values())
            accounts[f"account{account}"] = value

            if sum(accounts.values()) == 100:
                break

        await ControllerServerClient.send_splits(accounts)
        await sleep(30)


@app.on_event("startup")
async def on_startup() -> None:
    await send_splits()
