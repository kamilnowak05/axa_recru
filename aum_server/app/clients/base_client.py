from enum import Enum
from typing import Any, Dict, Optional

from fastapi import HTTPException, status
from httpx import AsyncClient, ConnectError, HTTPStatusError, Response, TimeoutException
from loguru import logger
from pydantic import AnyHttpUrl

import constants


class Methods(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class BaseHttpClient:
    def __init__(self, base_url: AnyHttpUrl) -> None:
        self.base_url = base_url

    async def _request(
        self,
        method: Methods,
        error_msg: str,
        endpoint: str,
        *args: Any,
        cookies: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        **kwargs: Any,
    ) -> Response:
        async with AsyncClient(base_url=self.base_url) as client:
            try:
                if not headers:
                    headers = {}

                headers[constants.INTERNAL_TOKEN_HEADER] = constants.INTERNAL_JWT
                response = await client.request(
                    method.value,
                    endpoint,
                    cookies=cookies,
                    headers=headers,
                    *args,
                    **kwargs,
                )
                response.raise_for_status()
                return response

            except ConnectError as e:
                logger.error(error_msg)
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE
                ) from e

            except TimeoutException as e:
                logger.error(f"{self.__class__.__name__} communication timeout!")
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE
                ) from e

            except HTTPStatusError as e:
                logger.error(f"{error_msg}: {e}")
                raise HTTPException(
                    status_code=response.status_code,
                    detail=response.json().get("detail"),
                ) from e
