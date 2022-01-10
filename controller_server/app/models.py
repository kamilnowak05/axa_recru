from decimal import Decimal
from enum import Enum

from pydantic import BaseModel


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
    quantity: int


class Account(BaseModel):
    name: str
    value: int
