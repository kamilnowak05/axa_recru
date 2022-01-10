from asyncio import sleep
from random import randrange
from typing import List

from fastapi import FastAPI
from loguru import logger

from app.clients.controller_server_client import ControllerServerClient
from app.models import Account

app = FastAPI()


async def send_splits() -> None:
    for _ in range(25):
        accounts: List[Account] = []
        for account in range(randrange(0, 100)):
            value = randrange(100)
            accounts_values_sum = sum(account.value for account in accounts)

            if accounts_values_sum + value > 100:
                value = 100 - accounts_values_sum
            accounts.append(Account(name=f"account{account}", value=value))

            if sum(account.value for account in accounts) != 100:
                continue

            logger.warning(f"sum: {sum(account.value for account in accounts)}")
            break
        await ControllerServerClient.send_splits(
            {account.name: account.value for account in accounts}
        )
        await sleep(30)


@app.on_event("startup")
async def on_startup() -> None:
    await send_splits()
