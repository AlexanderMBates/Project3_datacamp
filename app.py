from flask import Flask,jsonify
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps


app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'Wine'
COLLECTION_NAME = 'Wine_data'
FIELDS = {"country":True,"US":True,"description":True,"points":True,"price":True,"variety":True,"winery":True,"totalwords":True,"descriptivewords":True}

@app.route("/")
def welcome():
    return render_template('welcome.html')

    

@app.route("/index")
def index():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=89125 )

    
    # return json.dumps(projects, default=json_util.default)
    json_projects = []
    for project in projects:
        del project["_id"]
        json_projects.append(project)
    #json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return jsonify(json_projects)
    

if __name__ == "__main__":
    
    app.run(debug=True)
    # app.logger.info("test")