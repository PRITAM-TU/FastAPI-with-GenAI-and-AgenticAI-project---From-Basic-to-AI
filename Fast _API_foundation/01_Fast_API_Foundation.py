from fastapi import FastAPI
import uvicorn
from fastapi import Request


app=FastAPI(
    title="FastAPI Foundation",
    description="This is a FastAPI foundation project",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",


)

#Creat endpoint for root path
@app.get("/")
def root():
    return {"message":"Welcome to FastAPI Foundation project",
            
            "status":"success",
            "version":"1.0.0"
            }



#Ctreat another endpoint for /about path 
@app.get("/about")
def about():
    return {"message":"This is a FastAPI foundation project",
            "status":"success",
            "version":"1.0.0"
            }


# Check the Request libary in fastapi
@app.get("/debud/info-about-request")
def inforequest(request:Request):
    """   we want to check the info request where is comming from and what data they are send   """
    return {
        "Method":request.method,
        "PATH":str(request.url),
        "Header":dict(request.headers),
        "path_params":request.path_params,
        "query_params":request.query_params

    }



if __name__=="__main__":
    uvicorn.run("01_Fast_API_Foundation:app", host="127.0.0.1", port=8001, reload=True)

    """ Here we run our application uisng uvicorn cmd  which is  uvicorn app:"file name " --reload -- host  ---port """