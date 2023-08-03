from fastapi import FastAPI
from api.router.user import user_router

app: FastAPI = FastAPI()

app.include_router(user_router)


