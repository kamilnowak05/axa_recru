from fastapi import FastAPI, status

from app.models import Trade, Split

app = FastAPI()


@app.post("/trade", status_code=status.HTTP_200_OK)
async def fill_trade(data: Trade) -> None:
    pass


@app.post("/split", status_code=status.HTTP_200_OK)
async def split_to_accounts(data: Split) -> None:
    pass
