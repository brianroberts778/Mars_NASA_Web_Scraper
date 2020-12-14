from pymongo import MongoClient
from flask import Flask, render_template, redirect
import scrape_mars

conn = MongoClient("mongodb://localhost:27017/mars")

app = Flask(__name__)

# Create route to query mongoDB and pass data into html template
@app.route("/")
def index ():
    coll1 = conn.db.coll1.find_one()
    return render_template("index.html", mars_data = coll1) 

@app.route("/scrape")
def scrape():

    coll1 = conn.db.coll1
    scrape_data = scrape_mars.scrape()
    coll1.update({},scrape_data, upsert=True)
    return redirect ("/")

if __name__ == "__main__":
    app.run(Debug=True)



