from fastapi import APIRouter

from pydantic import BaseModel
from api.controllers.user import UserController

user_controller = UserController()

user_router = APIRouter(prefix="/user")

class TempBody(BaseModel):
    name:str

@user_router.get("")
async def get_all_user():
    return user_controller.get_all_user()

@user_router.post("/signup")
async def user_sign_up(body: TempBody):
    return user_controller.sign_up(body.name)

@user_router.post("/signin")
async def user_sign_in():
    return "USER SIGN IN!"




