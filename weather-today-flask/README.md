# Weather Today
## Flask/Python version
https://todays-weather.herokuapp.com/

A weather app using Python's Flask framework and the OpenWeather API to return the current weather in a city. Every request is also recorded in a PostgreSQL database.

Note: You should know how to use a Python virtual environment before using this app, have Postgresql installed on your machine (and know your username/password) and create a database named `weather-today`.

You will also need an account on [OpenWeather](https://openweathermap.org/api) (don't worry, it's free). Once signed in, select the API Keys tab. This is where your API key is that you will need later.

To use:
- Clone or download this repo to your local machine and `cd weather-today-flask`
- Make a file named `.env` and copy the `env_sample` file, replacing the API key with yours, and  you will also want to update the DATABASE_URL with your Postgresql username/password
- Activate your Python virtual environment
- Run `pip install -r requirements.txt` to install dependencies
- Make sure you have your `weather-today` database created, and run `flask db upgrade`
- Finally, run `flask run` to start the server and open your browser to `localhost:5000` to use the app.

Credits: Adapted from various tutorials
