from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Leeds Community Mapping API"}


def dev():
    uvicorn.run("main:app", reload=True)