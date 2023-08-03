

class TinyDBManager:
    __instance = None
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def create():
        ...
    def read():
        ...
    def update():
        ...
    def delete():
        ...