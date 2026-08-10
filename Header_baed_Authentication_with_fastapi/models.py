from sqlmodel import SQLModel,Field
from typing  import Optional



class data(SQLModel,table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    message: str


class Respons_data(SQLModel):
    message: Optional[str]