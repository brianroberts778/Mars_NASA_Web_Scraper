from pymongo import MongoClient
from flask import Flask, render_template, redirect
import mission_to_mars

conn = MongoClient("mongodb://localhost:27017/mars")

app = Flask(__name__)

@app.route("/")
def index ():
    coll1 = conn.db.coll1.find_one()
    return render_template("index.html", mars_data = coll1) 

@app.route("/scrape")
def scraper ():
    coll1 = conn.db.coll1
    scrape_data = mission_to_mars.scrape_info()
    coll1.update({},scrape_data, upsert=True)
    return redirect ("/")

app.run(Debug=True)


