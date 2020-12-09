import os
from flask import Flask

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

@app.route('/')
def DCM3():
    return "Data Centric Milestone3 Project"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=0)
