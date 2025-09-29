import jwt
from datetime import datetime, timezone, timedelta

def create_token(payload: dict, secret: str, exp_minutes: int = 15) -> str:

    try:
        payload.update({'exp':datetime.now(timezone.utc)} + timedelta(minutes=exp_minutes))
        return jwt.encode(payload, secret, algorithm = 'HS256')
    except Exception as token_ex:
        raise Exception('Token creation failed')

def decode_token(token: str, secret: str) -> dict:
    try:
        return jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.PyJWTError as e:
        raise Exception('Invalid or expired token') from e