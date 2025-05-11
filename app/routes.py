from flask import Flask
from flask_restful_swagger_3 import Api

from app.handlers.dashboard import Dashboard
from app.handlers.drive import Drives
from app.handlers.student import Students, Student


def create_app():
    app = Flask(__name__)
    api = Api(app)

    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
        return response

    api.add_resource(Dashboard, '/stats')
    api.add_resource(Students, '/students')
    api.add_resource(Student, '/students/<string:student_id>')
    api.add_resource(Drives, '/drives')

    return app
