from os.path import dirname, join

from pydantic import AnyHttpUrl, BaseSettings, Field, PositiveInt


class _Env(BaseSettings):
    class Config:
        env_file = join(dirname(__file__), ".env")
        env_file_encoding = "utf-8"

    PORT: PositiveInt = Field(8002, description="Port of this server")
    HOST: str = Field("localhost", description="Host of this server")
    SECRET: str = Field("change-me", description="secret for encoding and decoding JWT")

    CONTROLLER_SERVER_URL: AnyHttpUrl = Field(
        "http://localhost:8000", description="Controller server address"
    )


Env = _Env()
