from jose import JWTError, jwt
from app.config import JWT_SECRET

def encode_token(data: dict):
    return jwt.encode(data, JWT_SECRET, algorithm="HS256")

def decode_token(token: str):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except JWTError:
        return None
