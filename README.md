# Weather Today
A NodeJS CLI to get the current weather for any city

To use:  
Note: You should have NodeJS and npm installed on your machine already.
- Clone or download this repo to your local machine and `cd` into that directory
- Run `npm i` to install dependencies
- Make an account on [OpenWeather](https://openweathermap.org/api) (don't worry, it's free)
- Once signed in, select the API Keys tab and copy your default API key
- Run `export APIKEY=<apikey>` replacing `<apikey>` with your API key [Note: You will have to do this every time you open a new Terminal window/tab]
- Finally, run `node index.js -c <city>` to return the current temperature in that city.
