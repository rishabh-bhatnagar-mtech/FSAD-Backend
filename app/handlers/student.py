from flask import jsonify
from flask_restful import Resource


class Students(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "List students endpoint"})

    @staticmethod
    def post():
        return jsonify({"message": "Create student(s) endpoint"})


class Student(Resource):
    @staticmethod
    def get(id):
        return jsonify({"message": f"Get student {id}"})

    @staticmethod
    def put(id):
        return jsonify({"message": f"Update student {id}"})

    @staticmethod
    def patch(id):
        return jsonify({"message": f"Partial update student {id}"})

    @staticmethod
    def delete(id):
        return jsonify({"message": f"Delete student {id}"})
