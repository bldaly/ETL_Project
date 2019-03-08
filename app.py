from flask import Flask, render_template, redirect, Response, request
from flask_pymongo import pymongo

app= Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.restaurants_db


# Use flask_pymongo to set up mongo connection
# mongo=PyMongo(app, uri='mongodb://localhost:27017/restaurants_db')

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
    restaurants = db.restaurants.find()
    return render_template("load.html",
        restaurants=restaurants)





if __name__=='__main__':
    app.run(debug=True)