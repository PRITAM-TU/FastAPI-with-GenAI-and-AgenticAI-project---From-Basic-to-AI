import asyncio
import inspect
from datetime import date

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


@route.post("/trip")
async def create_trip(request: dict):
    """Create a trip summary and attach the destination weather forecast."""
    destination = request.get("destination", "")
    currency = request.get("currency", "")
    start_date = request.get("start_date")
    end_date = request.get("end_date")

    if isinstance(start_date, str):
        try:
            start_date = date.fromisoformat(start_date)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail="start_date must be a valid date") from exc
    if isinstance(end_date, str):
        try:
            end_date = date.fromisoformat(end_date)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail="end_date must be a valid date") from exc

    destination = destination.strip() if isinstance(destination, str) else ""
    currency = currency.strip().upper() if isinstance(currency, str) else ""

    if not destination:
        raise HTTPException(status_code=422, detail="destination must not be empty")
    if not currency or len(currency) != 3 or not currency.isalpha():
        raise HTTPException(status_code=422, detail="currency must be a 3-letter code")
    if start_date is None or end_date is None:
        raise HTTPException(status_code=422, detail="start_date and end_date are required")
    if end_date < start_date:
        raise HTTPException(status_code=422, detail="end_date must be on or after start_date")

    days = (end_date - start_date).days + 1
    cache_key = f"weather:{destination.casefold()}:{start_date}:{end_date}"
    place = None

    try:
        weather = get_cache(cache_key)
        if inspect.isawaitable(weather):
            weather = await weather
    except Exception:
        # A cache outage must not prevent fetching fresh weather data.
        weather = None

    if weather is None:
        try:
            weather_result = featch_weather(
                destination,
                start_date,
                end_date,
            )
            weather = (
                await weather_result
                if inspect.isawaitable(weather_result)
                else weather_result
            )

        except Exception as exc:
            raise HTTPException(
                status_code=502,
                detail=f"Unable to fetch weather data: {exc}",
            ) from exc

        try:
            cache_result = set_cache(cache_key, weather)
            if inspect.isawaitable(cache_result):
                await cache_result
            asyncio.create_task(_clear_cache_later(cache_key))
        except Exception:
            # Caching is optional; return the successfully fetched weather.
            pass
    try:
        from sevices.place_find import get_palce
            
        place_result = get_palce(destination)
        place = (
                                await place_result
                                if inspect.isawaitable(place_result)
                                else place_result
                        )
    except Exception :
        pass


    return {
        "destination": destination,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "days": days,
        "currency": currency,
        "weather": weather,
        "place": place,
    }


