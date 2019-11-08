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
    return render_template('countyDemo.html', options = get_state_options(counties), demo = get_interesting_demo(counties))
    
def get_state_options(counties):
    options = ""
    listOfStates = []
    for county in counties:
        if county['State'] not in listOfStates:
            listOfStates.append(county['State'])
            
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options
        
def get_interesting_demo(counties):
    max = counties[0]['Miscellaneous']['Veterans']
    county = counties[0]['County']
    for data in counties:
        if data['Miscellaneous']['Veterans'] > max:
            max = data['Miscellaneous']['Veterans']
            county = data['County']
    return county
    
if __name__=="__main__":
    app.run(debug=False, port=54321)