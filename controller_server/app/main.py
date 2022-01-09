from fastapi import FastAPI, status

from app.models import Trade

app = FastAPI()


@app.post("/trade", status_code=status.HTTP_200_OK)
async def fill_trade(data: Trade) -> None:
    pass
