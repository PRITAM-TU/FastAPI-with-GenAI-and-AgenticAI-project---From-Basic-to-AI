from fastapi import FastAPI
import uvicorn
from routes.planner import route as plan_router



app=FastAPI(
    title="This is yatra agents app",
    description="Agregated all the data like weather ,palce,currency "
)

@app.get("/")
def root():
    return{
        "message":"all the route are present "
    }
app.include_router(plan_router)


if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)