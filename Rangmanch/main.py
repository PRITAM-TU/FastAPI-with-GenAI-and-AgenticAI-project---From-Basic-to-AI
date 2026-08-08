from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn 
from database import create_db_and_tables
from routes.reviews import route as reviews_route

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform any setup tasks here
    create_db_and_tables()
    
    yield
    # Perform any cleanup tasks here
app=FastAPI(
    title="Rangmanch for review the feedback of the users",
    description="This is a feedback review application for users to provide their feedback and suggestions.",
    version="1.0.0",
    lifespan=lifespan
)
app.include_router(reviews_route)
#Create the Root endpoint 
@app.get("/")
def root():
    return {"message":"Welcome to Rangmanch application for feedback review"}

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
   