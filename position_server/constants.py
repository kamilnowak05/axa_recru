from jose import jwt

SERVICE_NAME: str = "position_server"
INTERNAL_TOKEN_HEADER: str = "x-internal-signature"
JWT_ALGORITHM = jwt.ALGORITHMS.HS256
