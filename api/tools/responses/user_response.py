from pydantic import BaseModel

class UserResponse(BaseModel):
    msg: str
    token: str|None = None




