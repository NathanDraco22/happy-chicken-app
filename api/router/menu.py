from typing import Annotated
from fastapi import APIRouter, UploadFile

menu_router = APIRouter(prefix="/menu")

@menu_router.get("")
async def get_all_menu_items():
    return "ALL ITEM HERE"

@menu_router.post("/upload-image")
async def upload_menu_image(file: UploadFile):
    print("esta llegando")
    return {"file received" : file.filename}



