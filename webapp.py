from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('countyDemo.html', options = get_state_options(counties))

@app.route("/fact")
def interesting_demo():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        state= request.args["state"]
    return render_template('countyDemo.html', options = get_state_options(counties), demo = get_interesting_demo(counties, state))
    
def get_state_options(counties):
    options = ""
    listOfStates = []
    for county in counties:
        if county['State'] not in listOfStates:
            listOfStates.append(county['State'])
            
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options
        
def get_interesting_demo(counties, state):
    states={}
    countyNum = ""
    for data in counties:
        if data["State"] not in states:
            states[data["State"]] = 1
        else:
            states[data["State"]] += 1
    if states[state] > 1:
        countyNum = state + " has " + str(states[state]) +  " counties."
    else:
        countyNum = state + " has " + str(states[state]) +  " county."
    return countyNum
    
if __name__=="__main__":
    app.run(debug=False, port=54321)