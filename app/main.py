from fastapi import FastAPI
from fastapi.responses import FileResponse

from pathlib import Path

app = FastAPI()


@app.get("/get_img/{img}")
async def get_image(img: str):
    image_path = Path("/srv/data/" + img)
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)
