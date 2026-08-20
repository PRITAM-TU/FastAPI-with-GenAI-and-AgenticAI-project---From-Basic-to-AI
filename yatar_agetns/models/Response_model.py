from pydantic import BaseModel
from datetime import date


class ResponseModel(BaseModel):
    message:str
    
    