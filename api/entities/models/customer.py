
class CustomerModel:
    name: str
    phone: str
    address: str

    def __init__(self, name: str, phone: str, address: str) :
        self.name = name
        self.phone = phone
        self.address = address