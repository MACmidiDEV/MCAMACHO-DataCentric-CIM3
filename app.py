import os
from flask import Flask, render_template

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

@app.route('/')                   

@app.route('/landing') 
def landing():
    return render_template("home.html") 

@app.route('/liveLearn')
def liveLearn():
    return render_template("liveLearn.html")  

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=0)
