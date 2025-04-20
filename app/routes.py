from flask import Flask
from flask_restful import Api

from app.handlers.auth import Sessions, Me
from app.handlers.dashboard import Dashboard
from app.handlers.drive import Drives, Drive
from app.handlers.report import ReportsVaccinations, ReportsExport
from app.handlers.student import Students, Student
from app.handlers.vaccination import Vaccinations, Vaccination, StudentVaccinations


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Sessions, '/sessions')
    api.add_resource(Sessions, '/sessions/<string:id>', endpoint='session')
    api.add_resource(Me, '/me')
    api.add_resource(Dashboard, '/dashboard')
    api.add_resource(Students, '/students')
    api.add_resource(Student, '/students/<string:id>')
    api.add_resource(Drives, '/drives')
    api.add_resource(Drive, '/drives/<string:id>')
    api.add_resource(Vaccinations, '/vaccinations')
    api.add_resource(Vaccination, '/vaccinations/<string:id>')
    api.add_resource(StudentVaccinations, '/students/<string:studentId>/vaccinations')
    api.add_resource(ReportsVaccinations, '/reports/vaccinations')
    api.add_resource(ReportsExport, '/reports/vaccinations/export')

    return app
