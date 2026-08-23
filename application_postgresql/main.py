"""FastAPI application entry point.

Run with:
	uvicorn main:app --reload
"""

from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from model import Todos
from database import engine


@asynccontextmanager
async def lifespan(_: FastAPI):
	"""Create database tables when the application starts."""
	Todos.metadata.create_all(bind=engine)
	yield


app = FastAPI(
	title="Application API",
	description="FastAPI server backed by PostgreSQL.",
	version="1.0.0",
	lifespan=lifespan,
)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=False,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/", tags=["system"])
async def root() -> dict[str, str]:
	return {"message": "API is running", "docs": "/docs"}


@app.get("/health", tags=["system"])
async def health() -> dict[str, Any]:
	return {
		"status": "ok",
		"service": "application-postgresql",
		"timestamp": datetime.now(timezone.utc).isoformat(),
	}


@app.exception_handler(Exception)
async def unhandled_exception_handler(_: Request, exc: Exception) -> JSONResponse:
	# Keep internal exception details out of production responses.
	return JSONResponse(
		status_code=500,
		content={"detail": "Internal server error"},
	)


if __name__ == "__main__":
	import uvicorn

	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
