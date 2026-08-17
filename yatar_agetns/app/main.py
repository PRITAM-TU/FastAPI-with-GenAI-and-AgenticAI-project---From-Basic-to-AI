from fastapi import FastAPI
import uvicorn

app=FastAPI()



@app.get("/")
def root():
    return{
        "message":"This is yatra agent",
        "version":"1.0.0",
        "endpoints":{
            "post/plane":"cretea plane for yatra using sse",
            "get/streem":"collect all data using SSE",
            "GET/catch-memory":"get all cache statictics ",
            "delete/cache":"delte all cache data"
        }
    }


if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)