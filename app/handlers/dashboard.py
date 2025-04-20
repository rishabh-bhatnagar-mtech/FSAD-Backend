from flask import jsonify
from flask_restful import Resource


class Dashboard(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "Dashboard endpoint"})
