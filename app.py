from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

NIDS = {
    "111" : "Pulak",
    "222" : "XYZ",
    "333" : "ABC"
}

def abort_if_nid_doesnt_exist(nidNo):
    if nidNo not in NIDS:
        return {"message" : "NID NO {} doesn't exist.".format(nidNo) },200


class TaskByNid(Resource):
    def get(self,nido):
        abort_if_nid_doesnt_exist(nidNo)
        name = NIDS["nidNo"]
        return { "message" : "NID NO: {} Name: {}".format(nidNo,name) },200

    def post(self,nidNo):
        return { "message" : "Inside post method" },200

    def put(self,nidNo):
        abort_if_nid_doesnt_exist(nid_no)
        return { "message" : "Inside put method" },200

    def delete(self,nidNo):
        abort_if_nid_doesnt_exist(nid_no)
        return { "message" : "Inside delete method" },200


class Task(Resource):
    
    def get(self):
        return { "message" : "Inside get method" },200

    def post(self):
        return { "message" : "Inside post method" },200

    def put(self):
        return { "message" : "Inside put method" },200

    def delete(self):
        return { "message" : "Inside delete method" },200


class TaskById(Resource):
    def get(self,taskId):
        return { "message" : "Inside get method of task id = {}".format(taskId) },200

    def post(self,taskId):
        return { "message" : "Inside post method of task id = {}".format(taskId) },200

    def put(self,taskId):
        return { "message" : "Inside put method of task id = {}".format(taskId) },200

    def delete(self,taskId):
        return { "message" : "Inside delete method of task id = {}".format(taskId) },200

api.add_resource(Task,"/task")
api.add_resource(TaskById,"/task/<string:taskId>")
api.add_resource(TaskByNid,"/task/nid/<string:nidNo>")

if __name__ == '__main__':
    app.run(debug=True)