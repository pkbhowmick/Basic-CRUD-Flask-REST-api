from flask import Flask, jsonify, request
from flask_restful import Resource,Api, request
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

app.url_map.strict_slashes = False

mongo = PyMongo(app)

# nidNo: [string]
# date of birth: [string],
# name english : [string],
# name bengali: [string],
# fathers name bengali: [string],
# mothers name bengali: [string],
# spouse name bengali: [string],
# present address: [string],
# permanent address: [string],
# nid front: [string(base 64 string)],
# nid back: [string(base 64 string)],
# picture: [string(base 64 string)]

def getValue(user):
    return {
        "nidNo" : user["nidNo"],
        "date of birth" : user["date of birth"],
        "name english" : user ["name english"],
        "name bengali" : user["name bengali"],
        "fathers name bengali" : user["fathers name bengali"],
        "mothers name bengali" : user["mothers name bengali"],
        "spouse name bengali" : user["spouse name bengali"],
        "present address" : user["present address"],
        "permanent address" : user["permanent address"],
        "nid front" : user["nid front"],
        "nid back" : user["nid back"],
        "picture" : user["picture"]
    }

def setValue():
    user = mongo.db.NIDS
    nidNo =  request.json["nidNo"]
    dateOfBirth = request.json["date of birth"]
    nameEnglish = request.json["name english"]
    nameBengali = request.json["name bengali"]
    fathersNameBengali = request.json["fathers name bengali"]
    mothersNameBengali = request.json["mothers name bengali"]
    spouseNameBengali = request.json["spouse name bengali"]
    presentAddress = request.json["present address"]
    permanentAddress = request.json["permanent address"]
    nidFront = request.json["nid front"]
    nidBack = request.json["nid back"]
    picture = request.json["picture"]

    newId = user.insert({
        "nidNo" : nidNo,
        "date of birth" : dateOfBirth,
        "name english" : nameEnglish,
        "name bengali" : nameBengali,
        "fathers name bengali" : fathersNameBengali,
        "mothers name bengali" : mothersNameBengali,
        "spouse name bengali" : spouseNameBengali,
        "present address" : presentAddress,
        "permanent address" : permanentAddress,
        "nid front" : nidFront,
        "nid back" : nidBack,
        "picture" : picture
    })
    newUser = user.find_one({"_id": newId})
    output = getValue(newUser)
    return output

def updateValue(user):

    for key in request.json.keys():
        user[key]=request.json[key]
    
    val = getValue(user)
    return val

class TaskByNid(Resource):
    def get(self,nidNo):
        nid = mongo.db.NIDS
        user = nid.find_one({'nidNo' : nidNo})
        if user:
            output = getValue(user)
        else:
            output = "Nid doesn't exist"

        return jsonify({'result' : output })

    def post(self,nidNo):
        nid = mongo.db.NIDS
        user = nid.find_one({'nidNo' : nidNo})
        if not user:
            output = setValue()
        else:
            output = "Nid already exists"

        return jsonify({'result' : output })

    def put(self,nidNo):
        nid = mongo.db.NIDS
        user = nid.find_one({'nidNo' : nidNo})
        if user:
            output = updateValue(user)
        else:
            output = "Nid doesn't exist"

        return jsonify({'result' : output })

    def delete(self,nidNo):
        nid = mongo.db.NIDS
        user = nid.find_one({"nidNo" : nidNo})
        if user:
            nid.remove({"nidNo" : nidNo})
            output = "Successfully deleted"
        else:
            output = "Nid doesn't exist"
        
        return jsonify({'result' : output })

api.add_resource(TaskByNid,"/task/nid/<string:nidNo>")


if __name__ == '__main__':
    app.run(debug=True)