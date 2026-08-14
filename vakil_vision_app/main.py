from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app:FastAPI):
    yield

app = FastAPI(
    title="VIKAL_VISION APP",
    description="ALL",
    version="1.0.0",
    lifespan=lifespan,
)
@app.get("/")
def root():
    return {
        "message":"name"
    }


if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)

