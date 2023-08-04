from typing import Protocol


class DBServicesProtocol(Protocol):
    def read(self) -> list[dict]:
        ...
    def create(self) -> str:
        ...
    def delete(self):
        ...
