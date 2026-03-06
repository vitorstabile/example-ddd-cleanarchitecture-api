from abc import ABC
from dataclasses import dataclass


@dataclass
class User(ABC):
    id: str
    username: str
