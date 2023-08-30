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
FIELDS = {"country":True,"US":True,"description":True,"points":True,"price":True,"variety":True,"winery":True,"total words":True,"descriptive words":True}

@app.route("/chart")
def chart():
    """displays chart"""

    return jsonify(justice_league_members)

@app.route("/")
def index():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=100)

    
    # return json.dumps(projects, default=json_util.default)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects
    

if __name__ == "__main__":
    
    app.run(debug=True)
    app.logger.info("test")