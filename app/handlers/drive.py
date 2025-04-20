from flask import jsonify
from flask_restful import Resource


class Drives(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "List drives endpoint"})

    @staticmethod
    def post():
        return jsonify({"message": "Create drive endpoint"})


class Drive(Resource):
    @staticmethod
    def get(id):
        return jsonify({"message": f"Get drive {id}"})

    @staticmethod
    def put(id):
        return jsonify({"message": f"Update drive {id}"})

    @staticmethod
    def patch(id):
        return jsonify({"message": f"Partial update drive {id}"})

    @staticmethod
    def delete(id):
        return jsonify({"message": f"Delete drive {id}"})
