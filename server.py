#!/usr/bin/env python
import os
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
app.config['base_uri'] = "http://product.christopher.su"

# ###################################################################
# Check if running locally on on Heroku and setup MongoDB accordingly
# ###################################################################
on_heroku = False
if 'MONGOLAB_URI' in os.environ:
  on_heroku = True

if on_heroku:
    client = MongoClient(os.environ['MONGOLAB_URI'])
    db = client.get_default_database()
    collection = db.data
else:
    client = MongoClient('mongodb://localhost:27017/')
    db = client.instachart
    collection = db.data

# ###################################################################
# Routes
# ###################################################################

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', header='Product Prompt', title='Product Prompt', jumbotron='''
        <p class="lead" id="prompt">Click the button below to get a product design prompt!</p>
        <p><a class="btn btn-lg btn-success" id="prompt-btn" href="#" role="button">Acquire Prompt</a></p>
        ''')

# ###################################################################
# Start Flask
# ###################################################################

if __name__ == '__main__':
    app.run(debug=True)