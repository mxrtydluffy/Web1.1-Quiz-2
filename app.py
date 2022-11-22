from flask import Flask, render_template, request
import json
import requests

# Configure app
app = Flask(__name__)

# Establish API URL
SWAPI_URL = 'https://swapi.py4e.com/api/'

#Establish app.route that will return result on main page.
@app.route('/')
def homepage():
    return render_template('home.html')

# Need to request data from the server and submit the data to be processed
@app.route('/results', methods=['GET', 'POST'])
def browse():
    if request.method == 'POST':
        character_id = request.form.get("character_index")
        character_info = requests.get(f'{SWAPI_URL}people/{character_id}')

        #Data that is being proceeded
        name = json.loads(character_info.content).get("name")
        height = json.loads(character_info.content).get("height")
        mass = json.loads(character_info.content).get("mass")
        hair_color = json.loads(character_info.content).get("hair_color")
        eye_color = json.loads(character_info.content).get("eye_color")
        homeworld = json.loads(character_info.content).get("homeworld")
        films = json.loads(character_info.content).get("films")

        # Information being presented
        content = {
            "name" : name,
            "height" : height,
            "mass" : mass,
            "hair_color" : hair_color,
            "eye_color" : eye_color,
            "homeworld" : homeworld,
            "films" : films
        }

        return render_template('home.html', **content)

    else:
        return render_template('home.html', **content)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)