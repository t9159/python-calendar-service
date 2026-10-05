from abc import ABC, abstractmethod
from typing import List
from models.person import Person


class BaseRepository(ABC):
    @abstractmethod
    def get_persons(self) -> List[Person]:
        pass