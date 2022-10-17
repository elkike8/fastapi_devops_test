import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="html", html=True), name="static")

# if __name__ == "__main__":
#     uvicorn.run(app)

# to run from command line uvicorn app:app
