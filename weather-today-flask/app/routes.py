from . import app
from flask import render_template, abort, redirect, url_for, session, g, make_response
from sqlalchemy.exc import IntegrityError
from .models import db, City
from .forms import CitySearchForm
from json import JSONDecodeError
import requests as req
import json
import os

def fetch_city_weather(city):
    """helper"""
    return req.get(f"{os.getenv('API_URL')}{city}&appid={str(os.getenv('API_KEY'))}&units=imperial")


@app.route('/', methods=['GET', 'POST'])
def home():
    form = CitySearchForm()

    if form.validate_on_submit():
        city = form.data['city_name']

        res = fetch_city_weather(city)
        try:
            session['context'] = res.text
            return redirect(url_for('.city_detail'))

        except JSONDecodeError:
            abort(404)

    return render_template('home.html', form=form)

@app.route('/city')
@app.route('/city/<city_name>')
def city_detail(city_name=None):

    if city_name:
        res = fetch_city_weather(city_name)
        return render_template('city_detail.html', **res.json())

    else:

        try:
            context = json.loads(session['context'])
            city = City(city_name=context['name'], temp=context['main']['temp'], description=context['weather'][0]['description'])
            db.session.add(city)
            db.session.commit()
            return render_template('city_detail.html', **context)
        except KeyError as e:
            print(e)
            res = make_response('Sorry, you did not enter a valid city. Go back and try again', 400)
            return res
