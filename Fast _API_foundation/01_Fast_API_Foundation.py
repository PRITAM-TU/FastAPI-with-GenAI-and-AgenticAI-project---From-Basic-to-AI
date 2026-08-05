from fastapi import FastAPI
import uvicorn


app=FastAPI(
    title="FastAPI Foundation",
    description="This is a FastAPI foundation project",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",


)

#Creat endpoint for root path
@app.get("/")
async def root():
    return {"message":"Welcome to FastAPI Foundation project",
            
            "status":"success",
            "version":"1.0.0"
            }



#Ctreat another endpoint for /about path 
@app.get("/about")
async def about():
    return {"message":"This is a FastAPI foundation project",
            "status":"success",
            "version":"1.0.0"
            }
         


if __name__=="__main__":
    uvicorn.run("01_Fast_API_Foundation:app", host="127.0.0.1", port=8001, reload=True)

    """ Here we run our application uisng uvicorn cmd  which is  uvicorn app:"file name " --reload -- host  ---port """