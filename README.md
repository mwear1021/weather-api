# Weather Command Center

## Description
A REST API that fetches and returns current weather data for a given city using the OpenWeatherMap API. Built with Flask and containerized with Docker.

## Features
- Returns current temperature, feels-like temperature, and weather conditions as JSON
- Accepts city name as a URL query parameter
- Dockerized for easy deployment

## Prerequisites
- Python 3.12+ or Docker
- OpenWeatherMap API key (free tier available)

## Installation (without Docker)
1. Clone this repository.
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```
4. Run the app:
   ```
   python app.py
   ```

## Installation (with Docker)
1. Clone this repository.
2. Create a `.env` file in the project root:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```
3. Build the image:
   ```
   docker build -t weather-app .
   ```
4. Run the container:
   ```
   docker run -p 5000:5000 --env-file .env weather-app
   ```

## Usage
Once running, hit the `/weather` endpoint with a `city` query parameter:
```
http://localhost:5000/weather?city=Pittsburgh
```

Example response:
```json
{
  "city": "Pittsburgh",
  "temperature": 72.3,
  "feels_like": 70.1,
  "conditions": "Clouds"
}
```

## Setup Notes
- Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
- Never commit your `.env` file -- it is listed in `.gitignore` and `.dockerignore`

## License
This project is open source. Feel free to use and modify.
