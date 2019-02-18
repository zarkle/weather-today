const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const app = express();

const apiKey = process.env.APIKEY;

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

app.get('/', function(req, res) {
  res.render('index', {weather: null, error: null});
});

app.post('/', function(req, res) {
  let city = req.body.city;
  let url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=imperial`

  request(url, function(err, response, body) {
    if(err){
      res.render('index', {weather: null, error: 'Sorry, there was an error. Please try again'});
    } else {
      let weather = JSON.parse(body);
      if(weather.main == undefined){
        res.render('index', {weather: null, error: 'Invalid city, please try again'});
      } else {
        let weatherText = `It is ${weather.main.temp.toFixed(0)} degrees F in ${weather.name}!`;
        res.render('index', {weather: weatherText, error: null});
      }
    }
  });
});

app.listen(3000, function() {
  console.log('Weather app listening on port 3000!');
});
