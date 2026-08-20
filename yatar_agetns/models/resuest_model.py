from pydantic import BaseModel
from datetime import date


class Requestmodel(BaseModel):
    destination:str
    start_date:date
    end_date:date
    currency:int | None = None 
