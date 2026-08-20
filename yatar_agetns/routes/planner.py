from datetime import date
import asyncio
import inspect

import httpx
from fastapi import APIRouter, HTTPException
from sevices.weather import featch_weather
from cache import get_cache, set_cache,clear_cache



route=APIRouter(
    prefix="/plan",
    tags=["Traval plan"]
)


async def _clear_cache_later(key: str) -> None:
    await asyncio.sleep(10)
    cache_result = clear_cache(key)
    if inspect.isawaitable(cache_result):
        await cache_result


@route.get("/")
async def planroot():
    return {
        "message":"Right now iam in plan endpoint "
    }


#Another route for take user input as respect to basemdoel and the chekc the data and calculate the trip how many days and and then call weather servicre


@route.post("/trip")
async def create_trip(request: dict):
    """Validate trip dates, calculate its duration, and return forecast data."""
    values = request
    destination = values.get("destination") or values.get("location")
    start_value = values.get("start_date") or values.get("from_date")
    end_value = values.get("end_date") or values.get("to_date")

    if not destination or not start_value or not end_value:
        raise HTTPException(
            status_code=422,
            detail="destination, start_date, and end_date are required",
        )

    try:
        start_date = date.fromisoformat(str(start_value))
        end_date = date.fromisoformat(str(end_value))
    except ValueError as exc:
        raise HTTPException(status_code=422, detail="Dates must use YYYY-MM-DD format") from exc

    days = (end_date - start_date).days
    if days <= 0:
        raise HTTPException(status_code=422, detail="end_date must be after start_date")
    key = f"{destination}@{start_date}@{end_date}"
    cached_trip = get_cache(key)
    if inspect.isawaitable(cached_trip):
        cached_trip = await cached_trip
    if cached_trip is not None:
        return cached_trip

    try:
        weather = await featch_weather(destination, start_date, end_date)
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Unable to fetch weather data",
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while fetching weather data",
        ) from exc

    trip = {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "days": days,
        "weather": weather,
    }
    cache_result = set_cache(key, trip)
    if inspect.isawaitable(cache_result):
        await cache_result
    asyncio.create_task(_clear_cache_later(key))
    return trip

