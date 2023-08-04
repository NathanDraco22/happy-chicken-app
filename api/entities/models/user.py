from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    password: str
    phone: str

    