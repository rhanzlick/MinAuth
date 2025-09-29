from abc import ABC, abstractmethod

class BaseDBAdapter(ABC):
    @abstractmethod
    def get_user(self, username: str) -> dict | None:
        ...
    
    @abstractmethod
    def create_user(self, username: str, password_hash: str) -> None:
        ...