'''first need to be import a python module'''
import datetime

from flask import Flask, render_template

app = Flask(__name__)

'''activate index route which is going to call index function'''
'''variable now, will hold datetime.now() module imported from python'''
'''boolean variable new_year, will defined if in fact is new year or not'''


@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", new_year=new_year)
