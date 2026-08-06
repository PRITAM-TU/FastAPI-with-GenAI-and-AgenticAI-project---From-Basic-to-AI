from pydantic import BaseModel
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    description: str
    availability: bool


class MenuResponse(BaseModel):
    message: str
    status: str
    count: int | None = None
    menu: list[MenuItem]