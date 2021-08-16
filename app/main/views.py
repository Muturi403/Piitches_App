from flask import render_template, redirect, url_for,abort,request
from . import main

@main.route('/')
def index():
    pitches = Pitch.query.all()
    sports = Pitch.query.filter_by(category = 'Sports').all()
    business = Pitch.query.filter_by(category = 'Business').all()
    technology = Pitch.query.filter_by(category = 'Technology').all() 
    return render_template('index.html', pitches = pitches,sports = sports, business = business, technology = technology)
  
