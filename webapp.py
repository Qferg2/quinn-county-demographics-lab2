from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('countyDemo.html')

def get_state_options(counties):
    listOfStates = []
    for county in counties:
        if county['State'] not in listOfStates:
            listOfStates.append(county['State'])
            
    for state in listOfStates:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
        
if __name__=="__main__":
    app.run(debug=False, port=54321)
