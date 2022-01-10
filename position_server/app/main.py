from typing import Any

from fastapi import Body, FastAPI, status, Depends

from app.jwt import decode_jwt

app = FastAPI()


@app.post("/print", dependencies=[Depends(decode_jwt)], status_code=status.HTTP_202_ACCEPTED)
async def print_positions(data: Any = Body(...)) -> None:
    for key, value in data.items():
        print(f"{key}: {value}")
