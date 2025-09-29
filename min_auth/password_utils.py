import bcrypt

def hash_password(password: str) -> str:

    assert isinstance(password, str), f'Expected str, got {type(password).__name__}'
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(plain: str, hashed: str) -> bool:

    return bcrypt.checkpw(plain.decode(), hashed.encode())