from typing import Dict

from fastapi import FastAPI, HTTPException, status

from app.models import Trade

app = FastAPI()


@app.post("/trade", status_code=status.HTTP_200_OK)
async def fill_trade(data: Trade) -> None:
    pass


@app.post("/split", status_code=status.HTTP_200_OK)
async def split_to_accounts(data: Dict[str, float]) -> None:
    if sum(data.values()) != 100:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Sum of percentages of all accounts should be equal to 100",
        )
