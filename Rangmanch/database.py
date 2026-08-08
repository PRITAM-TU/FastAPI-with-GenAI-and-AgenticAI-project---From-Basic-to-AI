from sqlmodel import SQLModel,Session,create_engine

DATABASE_URL="sqlite:///Rangmanch.db"
engine = create_engine(DATABASE_URL,echo=True)


def create_db_and_tables():
    """ create the database and tables if they do not exist """
    SQLModel.metadata.create_all(engine)


def get_session():
    """ create a new session for the database """
    with Session(engine) as session:
        yield session
