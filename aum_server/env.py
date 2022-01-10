from os.path import dirname, join

from pydantic import AnyHttpUrl, BaseSettings, Field, PositiveInt


class _Env(BaseSettings):
    class Config:
        env_file = join(dirname(__file__), ".env")
        env_file_encoding = "utf-8"

    PORT: PositiveInt = Field(8000, description="Port of this server")
    HOST: str = Field("localhost", description="host of this server")
    SECRET: str = Field("change-me", description="Secret for encoding and decoding JWT")

    CONTROLLER_SERVER_URL: AnyHttpUrl = Field(
        "http://localhost:8001", description="Controller server address"
    )


Env = _Env()
