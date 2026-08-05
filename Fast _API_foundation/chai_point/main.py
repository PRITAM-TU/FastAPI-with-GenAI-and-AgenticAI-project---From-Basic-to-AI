from fastapi import FastAPI
import uvicorn

app=FastAPI(
    title="Chai_point all menu",
    description="In bengaluru city one chai point present that serve the all menu that they have but they want to buid some api that send all the request related to that chai point",
    version='1.0.0',
    docs_url="/docs"

)

@app.get("/")
def Root():
    return {
        "all_menu": ["Sweet Chai", "Rosogolla Chai"],
        "status": "success"
    }
@app.get("/about")
def about():
    return {
        "message": "This is a chai point project",
        "status": "success",
        "version": "1.0.0"
    }


if __name__=="__main__":
     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

