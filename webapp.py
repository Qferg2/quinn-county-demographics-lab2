from flask import Flask, request, Markup, render_template, flsh, Markup
import os
import json
app = Flask(__name__)

if __name__=="__main__":
    app.run(debug=False, port=54321)