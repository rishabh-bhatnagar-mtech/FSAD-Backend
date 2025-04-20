from flask import Flask, jsonify
from flask_restful import Api, Resource


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


class Dashboard(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "Dashboard endpoint"})


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


class ReportsVaccinations(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "List vaccination reports"})


class ReportsExport(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "Export reports endpoint"})


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
