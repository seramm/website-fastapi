from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from .routers import health
from pathlib import Path

app = FastAPI()

app.include_router(health.router)

app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )

@app.get("/get_img/{img}")
async def get_image(img: str):
    image_path = Path("/srv/data/" + img)
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)

@app.get("/get_n_img/")
async def get_n_imgs():
    path = Path("/srv/data/")
    n = len([f for f in path.iterdir() if f.is_file()])
    return {"number": n}
