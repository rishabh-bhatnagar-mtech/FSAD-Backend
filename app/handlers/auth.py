from flask import jsonify
from flask_restful import Resource


class Sessions(Resource):
    @staticmethod
    def post():
        return jsonify({"message": "Login endpoint"})

    @staticmethod
    def delete(id):
        return jsonify({"message": f"Logout endpoint {id}"})


class Me(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "Current user endpoint"})
