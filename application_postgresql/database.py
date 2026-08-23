import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Load the root project's .env even when Uvicorn is started from another directory.
load_dotenv()

# Example: postgresql+psycopg2://user:password@localhost:5432/database
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
	DATABASE_URL = URL.create(
		drivername="postgresql",
		username=os.getenv("POSTGRES_USER", "postgres"),
		password=os.getenv("POSTGRES_PASSWORD", "pritamtung2005"),
		host=os.getenv("POSTGRES_HOST", "localhost"),
		port=int(os.getenv("POSTGRES_PORT", "5432")),
		database=os.getenv("POSTGRES_DB", "postgres"),
	)


engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
	"""Provide a database session for FastAPI dependencies."""
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
