import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env
  
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')                   

@app.route('/landing') 
def landing():
    return render_template("home.html") 

@app.route('/liveLearn')
def liveLearn():
    return render_template("liveLearn.html")  

@app.route('/getLearning')         
def getLearn():
    return render_template("learningLinks.html", LearningLinks=mongo.db.LearningLinks.find())   

@app.route('/add_link')
def add_link():
    return render_template('addLink.html',
                           Categories=mongo.db.Categories.find())        

@app.route('/insert_link', methods=['POST'])
def insert_link():
    LearningLinks = mongo.db.LearningLinks   
    LearningLinks.insert_one(request.form.to_dict())    
    return redirect(url_for('getLearning'))    

@app.route('/edit_link/<link_id>')
def edit_link(link_id):
    the_link = mongo.db.LearningLinks.find_one({"_id": ObjectId(link_id)})
    all_categories =  mongo.db.Categories.find()
    return render_template('editLink.html', link=the_link, Categories=all_categories)

 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=0)
