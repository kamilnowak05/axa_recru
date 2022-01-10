from pydantic import BaseModel


class Account(BaseModel):
    name: str
    value: int
