from fastapi import APIRouter



route=APIRouter(prefix="/auth",tags=["all end point with auth "])


@route.get("/")
def auth():
    return {
        "message":"ALL end point with auth route "
    }