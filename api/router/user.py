from fastapi import APIRouter
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from api.controllers.user import UserController

from api.entities.models.user import UserModel

user_controller = UserController()

user_router = APIRouter(prefix="/user")

@user_router.get("")
async def get_all_user():
    return user_controller.get_all_user()

@user_router.post("/signup")
async def user_sign_up(body: UserModel):
    return user_controller.sign_up(body)

@user_router.post("/signin")
async def user_sign_in():
    return "USER SIGN IN!"




