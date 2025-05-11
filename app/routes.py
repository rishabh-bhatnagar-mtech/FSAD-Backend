from flask import Flask
from flask_restx import Api

from app.handlers.dashboard import api as dashboard_ns
from app.handlers.drive import api as drives_ns
from app.handlers.student import api as students_ns


def create_app():
    app = Flask(__name__)
    api = Api(app, doc='/api/swagger', title='Vaccination API', version='1.0')

    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
        return response

    api.add_namespace(dashboard_ns)
    api.add_namespace(drives_ns)
    api.add_namespace(students_ns)

    return app
