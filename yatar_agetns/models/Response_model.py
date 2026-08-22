from pydantic import BaseModel
from datetime import date


class ResponseModel(BaseModel):
    message:str
class place_find(BaseModel):
    name: str
    city: str
    description: str
    rating: float = 0.0
class TripRequest(BaseModel):
    destination: str | None=None
    start_date: date | None=None
    end_date: date   | None=None
    currency: str    | None=None

