from flask import Flask, render_template, redirect, Response, request
from flask_pymongo import PyMongo

app= Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo=PyMongo(app, uri='mongodb://localhost:27017/restaurants_db')

@app.route('/')
def index():
    
    return render_template('index.html')
   

@app.route('/extract')
def extract():
    
    return render_template('index.html')


@app.route('/transform')
def transform():
    return render_template('index.html')

@app.route('/load')
def load():
    mars_data = scrape_mars.scrape()
    mars= mongo.db.mars
    mars.update({}, mars_data, upsert=True)


if __name__=='__main__':
    app.run(debug=True)