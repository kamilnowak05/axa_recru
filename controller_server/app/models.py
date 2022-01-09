from decimal import Decimal
from enum import Enum
from typing import List

from fastapi import status, HTTPException
from pydantic import BaseModel, validator


class StockTickerEnum(Enum):
    agilent_technologies = "A"
    apple = "AAPL"
    berkshire_hathaway = "BRK"
    axa = "CS"
    alphabet = "GOOG"
    harley_davidson = "HOG"
    hewlett_packard = "HPQ"
    intel = "INTC"
    microsoft = "MSFT"
    petco = "WOOF"


class Trade(BaseModel):
    stock_ticker: StockTickerEnum
    price: Decimal
    quantity: float


class SplitAccount(BaseModel):
    name: str
    percent: float


class Split(BaseModel):
    accounts: List[SplitAccount]

    @validator("accounts")
    def check_percentage_split(cls, v: List[SplitAccount]) -> None:
        if sum(account.percent for account in v) != 100:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Sum of percentages of all accounts should be equal to 100")
