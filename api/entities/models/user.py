
class UserModel:
    name: str
    password: str
    phone: str

    def __init__(self, name: str, password: str, phone: str):
        self.name = name
        self.password = password
        self.phone = phone
