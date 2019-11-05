from flask import Flask, request, Markup, render_template, flsh, Markup
import os
import json
app = Flask(__name__)

def get_state_options
    listOfStates = []
    for county in counties:
        if county['State'] not in listOfStates:
            listOfStates.append(county['State'])
            
    for 


if __name__=="__main__":
    app.run(debug=False, port=54321)
