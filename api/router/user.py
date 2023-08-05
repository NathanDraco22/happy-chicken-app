from fastapi import APIRouter, Response

from pydantic import BaseModel
from api.controllers.user import UserController

from api.entities.models.user import UserModel

user_controller = UserController()

user_router = APIRouter(prefix="/user")

@user_router.get("")
async def get_all_user():
    return user_controller.get_all_user()

@user_router.post("/signup")
async def user_sign_up(body: UserModel, res: Response):
    model, res.status_code = user_controller.sign_up(body) 
    return model

@user_router.post("/signin")
async def user_sign_in():
    return "USER SIGN IN!"




