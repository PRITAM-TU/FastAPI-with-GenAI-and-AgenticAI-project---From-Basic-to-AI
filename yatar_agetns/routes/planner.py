from fastapi import APIRouter
from models.resuest_model import Requestmodel



route=APIRouter(
    prefix="/plan",
    tags=["Traval plan"]
)


@route.post("/")
async def Traval_pane(traval_detail:Requestmodel):
    """ Agregated all the data loke weather and place and curency converter like that   """
    data=Requestmodel(traval_detail.model_dump())
    if not data:
        return{
            "error":"No data send form client "
        }
    return  {
        "Message":"Suscesfully"
    }