from .password_utils import hash_password, verify_password
from .token_utils import create_token, decode_token
from .db_adapter import BaseDBAdapter

class AuthService:

    def __init__(self, db: BaseDBAdapter, jwt_secret: str):
        self.db = db
        self.jwt_secret = jwt_secret

    def register(self, username: str, password: str) -> None:
        hashed_pass = hash_password(password)
        self.db.create_user(username, hashed_pass)
    
    def login(self, username: str, password: str) -> str:
        
        user = self.db.get_user(username, password)
        if not user:
            raise Exception('User not found')
        if not verify_password(password, user.get('password')):
            raise Exception('Invalid password')
        return create_token({'sub': str(username)}, self.jwt_secret)
    
    def verify(self, token: str) -> dict:
        return decode_token(token, self.jwt_secret)