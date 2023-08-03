from fastapi import APIRouter

user_router = APIRouter(prefix="/user")

@user_router.get("")
async def get_all_user():
    return "ALL USERS!"

@user_router.post("/signup")
async def user_sign_up():
    return "USER SIGN UP!"

@user_router.post("/signin")
async def user_sign_in():
    return "USER SIGN IN!"




