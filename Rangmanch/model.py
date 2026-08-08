from sqlmodel import SQLModel,Field
class Feedback(SQLModel,table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    message: str


class FeedbackCreate(SQLModel):
    name: str
    email: str
    message: str


class FeedbackUpdate(SQLModel):
    email: str
    message: str

class FeedbackRead(SQLModel):
    id: int
    name: str
    email: str
    message: str


class FeedbackDelete(SQLModel):
    id:int


class Response_delete(SQLModel):
    message:str

