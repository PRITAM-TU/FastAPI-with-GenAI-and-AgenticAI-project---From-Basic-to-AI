from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from routes.route import route as head_route
from database import get_session,creat_database


@asynccontextmanager
async def lifespan(app:FastAPI):
    creat_database()

    yield

app=FastAPI(
    title="Header based Authentication with fast api",
    description="Before data respons we want to Authenticate the end_point",
    lifespan=lifespan
)
app.include_router(head_route)


@app.get("/", tags=["root route"])
def root():
    return {
        "message":"Wellcome to Header based Authentication End point"
    }
if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
