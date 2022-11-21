from flask import Flask, request, render_template
import random
import json

# Configure app
app = Flask(__name__)

# Establish API URL
SWAPI = 'https://swapi.py4e.com/api/'

#Establish app.route