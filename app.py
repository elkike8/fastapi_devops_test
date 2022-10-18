import uvicorn

# from fastapi import APIRouter, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates


# templates = Jinja2Templates(directory="html")

# general_pages_router = APIRouter()

# @general_pages_router.get("/")
# async def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="html", html=True), name="static")

# if __name__ == "__main__":
#     uvicorn.run(app)

# to run from command line uvicorn app:app
#
