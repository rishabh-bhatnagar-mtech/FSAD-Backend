from flask import jsonify
from flask_restful import Resource


class ReportsVaccinations(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "List vaccination reports"})


class ReportsExport(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "Export reports endpoint"})
