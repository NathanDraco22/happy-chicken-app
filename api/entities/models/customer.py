from pydantic import BaseModel

class CustomerModel(BaseModel):
    name: str
    phone: str
    address: str