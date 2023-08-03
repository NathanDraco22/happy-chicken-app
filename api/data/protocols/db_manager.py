from typing import Protocol

class DBManagerProtocol(Protocol):
    def create():
        ...
    def read():
        ...
    def update():
        ...
    def delete():
        ...



