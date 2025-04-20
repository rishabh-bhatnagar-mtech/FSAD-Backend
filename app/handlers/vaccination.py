from flask import jsonify
from flask_restful import Resource


class Vaccinations(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "List vaccinations endpoint"})

    @staticmethod
    def post():
        return jsonify({"message": "Create vaccination endpoint"})


class Vaccination(Resource):
    @staticmethod
    def get(id):
        return jsonify({"message": f"Get vaccination {id}"})

    @staticmethod
    def put(id):
        return jsonify({"message": f"Update vaccination {id}"})

    @staticmethod
    def delete(id):
        return jsonify({"message": f"Delete vaccination {id}"})


class StudentVaccinations(Resource):
    @staticmethod
    def post(student_id: str):
        return jsonify({"message": f"Create vaccination for student {student_id}"})
