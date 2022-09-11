from abc import ABC
from abc import abstractmethod
from src.entity.example_sqlite_enti import ExampleSqlite

class ExampleRepositoryInterface(ABC):
    @abstractmethod
    def example(self) -> str:
        ...

    @abstractmethod
    def example_sqlite(self) -> ExampleSqlite:
        ...

