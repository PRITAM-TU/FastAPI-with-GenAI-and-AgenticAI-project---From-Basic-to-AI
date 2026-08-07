from fastapi import FastAPI
import uvicorn





app=FastAPI(
    title="Pincode Lookup",
    description="This API allows you to look up information based on Indian pincodes.",
    version="1.0.0",
    
)

#creat the root endpoint 
@app.get("/")
def root( ):
    return {"message":"Welcome to the Pincode Lookup API."}




if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8001,reload=True)
