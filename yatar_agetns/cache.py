from typing import Any


# In-memory cache keyed by a location (or any other weather request key).
_cache: dict[str, Any] = {}


async def get_cache(key: str) -> Any | None:
    """Return cached weather data for *key*, or ``None`` when it is missing."""
    return _cache.get(key)


async def set_cache(key: str, value: Any) -> Any:
    """Cache and return weather data for *key*."""
    _cache[key] = value
    return value


async def clear_cache() -> None:
    """Remove all cached weather data."""
    _cache.clear()
