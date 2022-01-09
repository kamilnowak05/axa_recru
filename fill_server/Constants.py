from datetime import datetime

from jose import jwt

from Env import Env

SERVICE_NAME: str = "fill_server"
INTERNAL_TOKEN_HEADER: str = "x-internal-signature"
JWT_ALGORITHM = jwt.ALGORITHMS.HS256


def generate_internal_jwt() -> str:
    claims = {"iss": SERVICE_NAME, "iat": datetime.now().timestamp()}
    return jwt.encode(claims, key=Env.SECRET, algorithm=JWT_ALGORITHM)


INTERNAL_JWT: str = generate_internal_jwt()
