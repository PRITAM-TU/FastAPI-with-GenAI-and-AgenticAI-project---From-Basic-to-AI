from fastapi import APIRouter



route=APIRouter(
    prefix="/plan",
    tags=["Traval plan"]
)


@route.get("/")
async def Traval_pane():
    """ Agregated all the data loke weather and place and curency converter like that   """
    return  {
        "Message":"Suscesfully"
    }