from pydantic import BaseModel

class UserResponse(BaseModel):
    userId: str|None = None
    msg: str
    token: str|None = None




