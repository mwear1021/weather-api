# Weather Command Center

A Flask REST API that fetches and returns current weather data for a given city using the OpenWeatherMap API. Containerized with Docker and deployed on Render with a full CI/CD pipeline via GitHub Actions.

**Live:** https://weathercommandcentercli.onrender.com

## Features
- Returns current temperature, feels-like temperature, and weather conditions as JSON
- Accepts city name as a URL query parameter
- Defaults to New York if no city is provided
- Dockerized for easy local and cloud deployment
- CI/CD pipeline with automated security scanning, linting, smoke testing, and deployment

## CI/CD Pipeline
Every push to `main` triggers a GitHub Actions workflow that:
1. Installs dependencies
2. Runs Bandit security scanning
3. Runs flake8 linting
4. Runs a smoke test against the live API
5. Triggers a Render deploy if all checks pass

## Prerequisites
- Python 3.12+ or Docker
- OpenWeatherMap API key (free tier available at [openweathermap.org](https://openweathermap.org/api))

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
Hit the `/weather` endpoint with a `city` query parameter:
```
GET /weather?city=Pittsburgh
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

If no city is provided, defaults to New York:
```
GET /weather
```

## Security Notes
- Never commit your `.env` file -- it is listed in `.gitignore` and `.dockerignore`
- Bandit security scanning runs automatically on every push via GitHub Actions

## License
This project is open source. Feel free to use and modify.
