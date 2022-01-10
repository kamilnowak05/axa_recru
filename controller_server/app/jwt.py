from typing import Any, Dict

from fastapi import HTTPException, status, Header
from jose import ExpiredSignatureError, JWTError, jwt
from loguru import logger

import constants
from env import Env


def decode_jwt(token: str = Header(None, alias=constants.INTERNAL_TOKEN_HEADER)) -> Dict[str, Any]:
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    try:
        return jwt.decode(token, Env.SECRET, algorithms=constants.JWT_ALGORITHM)

    except ExpiredSignatureError:
        logger.debug("Token is expired")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired"
        )
    except JWTError:
        logger.debug("Token is invalid")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
