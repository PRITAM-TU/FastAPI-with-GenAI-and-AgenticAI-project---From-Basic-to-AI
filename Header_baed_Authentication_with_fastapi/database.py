from sqlmodel import SQLModel,Session,create_engine
from typing import Optional

DATABASE_URL="sqlite:///data.db"
engine=create_engine(DATABASE_URL,echo=True)


def creat_database():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine)  as session:
        yield session

