from os.path import dirname, join

from pydantic import BaseSettings, Field, PositiveInt


class _Env(BaseSettings):
    class Config:
        env_file = join(dirname(__file__), ".env")
        env_file_encoding = "utf-8"

    PORT: PositiveInt = Field(8002, description="Port of this server")
    HOST: str = Field("localhost", description="host of this server")


Env = _Env()
