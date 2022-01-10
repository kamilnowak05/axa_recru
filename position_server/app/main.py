from typing import Any

from fastapi import Body, FastAPI, status

app = FastAPI()


@app.post("/print", status_code=status.HTTP_202_ACCEPTED)
async def print_positions(data: Any = Body(...)) -> None:
    for key, value in data.items():
        print(f"{key}: {value}")
