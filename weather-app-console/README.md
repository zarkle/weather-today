# Weather Today
A Node.js CLI to get the current temperature for any city.

To use:  
**Reminder: You should have Node.js and npm installed on your machine and an account on OpenWeather.
- Clone or download this repo to your local machine and `cd` into the weather-app-console directory
- Run `npm i` to install dependencies
- If you haven't yet, make an account on [OpenWeather](https://openweathermap.org/api) (don't worry, it's free)
- Once signed in to OpenWeather, select the API Keys tab and copy your default API key
- Run `export APIKEY=<apikey>` replacing `<apikey>` with your API key [Note: You will have to do this every time you open a new Terminal window or tab]
- Finally, run `node index.js -c <city>` to return the current temperature in that city (in Fahrenheit).
