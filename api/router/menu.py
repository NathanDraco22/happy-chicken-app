import os
import shutil
from urllib.parse import urlsplit, urljoin
from fastapi import APIRouter, UploadFile, Request

menu_router = APIRouter(prefix="/menu")

@menu_router.get("")
async def get_all_menu_items():
    return "ALL ITEM HERE"

@menu_router.post("/upload-image")
async def upload_menu_image(req: Request,file: UploadFile):
    dir_path = os.path.join(os.getcwd(), "static", "images", file.filename)
    with open(dir_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    splited = urlsplit(req.url._url)
    base = f"{splited[0]}://{splited[1]}"
    img_path = f"/assets/images/{file.filename}"
    img_url = urljoin(base,img_path)
    return {
        "url" : img_url,
        "file received" : file.filename
    }



