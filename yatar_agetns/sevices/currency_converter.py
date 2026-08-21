import asyncio
import json
import logging
import os
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def _normalize_currency_code(currency: str) -> str:
    """Validate and normalize an ISO 4217 currency code."""
    if not isinstance(currency, str):
        raise ValueError("currency must be a string")

    currency_code = currency.strip().upper()
    if len(currency_code) != 3 or not currency_code.isalpha():
        raise ValueError("currency must be a three-letter ISO currency code")
    return currency_code


def _fetch_exchange_rate(currency_code: str) -> float:
    """Fetch the USD exchange rate for a given ISO currency code."""
    api_key = os.getenv("CURRENCY_CONVERTER_API")
    if not api_key:
        raise RuntimeError("CURRENCY_CONVERTER_API is not configured")

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    request = Request(url, headers={"User-Agent": "currency-converter/1.0"})

    try:
        with urlopen(request, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError) as exc:
        logger.exception("Failed to fetch exchange rates for %s", currency_code)
        raise RuntimeError("Unable to fetch exchange rates") from exc

    if payload.get("result") != "success":
        error_type = payload.get("error-type", "Exchange-rate request failed")
        raise RuntimeError(error_type)

    conversion_rates = payload.get("conversion_rates")
    if not isinstance(conversion_rates, dict):
        raise RuntimeError("Exchange-rate response is invalid")

    if currency_code not in conversion_rates:
        raise ValueError(f"Unsupported currency: {currency_code}")

    try:
        return float(conversion_rates[currency_code])
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"Invalid exchange rate for currency: {currency_code}") from exc


async def currency_converter(currency: str) -> float:
    """Return the USD exchange rate for the requested ISO currency code."""
    currency_code = _normalize_currency_code(currency)
    return await asyncio.to_thread(_fetch_exchange_rate, currency_code)

