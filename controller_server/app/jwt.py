from typing import Any, Dict

from fastapi import HTTPException, status
from jose import ExpiredSignatureError, JWTError, jwt
from loguru import logger

import constants
from env import Env


def decode_jwt(token: str, secret: str = Env.SECRET) -> Dict[str, Any]:
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    try:
        return jwt.decode(token, secret, algorithms=constants.JWT_ALGORITHM)

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
