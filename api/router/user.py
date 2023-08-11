from fastapi import APIRouter, Response

from api.controllers.user import UserController
from api.entities.models.user import UserModel
from api.entities.dtos.signin import SigninDTO
from api.tools.responses.user_response import UserResponse

__endpoint_settings = {
    "response_model" : UserResponse,
    "response_model_exclude_none" : True
}

user_controller = UserController()

user_router = APIRouter(prefix="/user")

@user_router.get("")
async def get_all_user():
    return user_controller.get_all_user()

@user_router.post("/signup", **__endpoint_settings)
async def user_sign_up(body: UserModel, res: Response):
    model, res.status_code = user_controller.sign_up(body) 
    return model

@user_router.post("/signin", **__endpoint_settings)
async def user_sign_in(body: SigninDTO, res: Response):
    model, res.status_code = user_controller.sign_in(body)
    return model




