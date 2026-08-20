from datetime import date
import os
from dotenv import load_dotenv
load_dotenv()

import httpx


async def featch_weather(destination: str, star_date: date, end_Date: date):
	"""Fetch and return OpenWeather forecast data for a destination and date range."""
	if star_date > end_Date:
		raise ValueError("star_date must be on or before end_Date")

	api_key = os.getenv("OPENWEATHER_API_KEY")
	if not api_key:
		raise RuntimeError("OPENWEATHER_API_KEY environment variable is not set")

	async with httpx.AsyncClient(timeout=10.0) as client:
		response = await client.get(
			"https://api.openweathermap.org/data/2.5/forecast",
			params={
				"q": destination,
				"appid": api_key,
				"units": "metric",
			},
		)
		response.raise_for_status()
		weather = response.json()

	weather["list"] = [
		item
		for item in weather.get("list", [])
		if star_date <= date.fromisoformat(item["dt_txt"].split(" ", 1)[0]) <= end_Date
	]
	return weather
    


