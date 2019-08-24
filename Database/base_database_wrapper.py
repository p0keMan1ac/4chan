from abc import ABC, abstractmethod


class BaseDatabaseWrapper(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
