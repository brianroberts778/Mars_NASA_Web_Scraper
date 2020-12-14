from pymongo import MongoClient
from flask import Flask, render_template, redirect
import scrape_mars

mongo = MongoClient("mongodb://localhost:27017/mars")

app = Flask(__name__)

# Create route to query mongoDB and pass data into html template
@app.route("/")
def index ():

    final_dict = mongo.db.final_dict.find_one()
    return render_template("index.html", mars_data = final_dict) 

@app.route("/scrape")
def scrape():

    final_dict = mongo.db.final_dict
    scrape_data = scrape_mars.scrape()
    final_dict.update({}, scrape_data, upsert=True)
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)



