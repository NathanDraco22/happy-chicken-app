from pydantic import BaseModel

class SigninDTO(BaseModel):
    phone: str
    password: str



