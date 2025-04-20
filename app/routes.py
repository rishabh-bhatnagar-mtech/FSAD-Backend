from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Sessions(Resource):
    def post(self):
        return jsonify({"message": "Login endpoint"})

    def delete(self, id):
        return jsonify({"message": f"Logout endpoint {id}"})


class Me(Resource):
    def get(self):
        return jsonify({"message": "Current user endpoint"})


class Dashboard(Resource):
    def get(self):
        return jsonify({"message": "Dashboard endpoint"})


class Students(Resource):
    def get(self):
        return jsonify({"message": "List students endpoint"})

    def post(self):
        return jsonify({"message": "Create student(s) endpoint"})


class Student(Resource):
    def get(self, id):
        return jsonify({"message": f"Get student {id}"})

    def put(self, id):
        return jsonify({"message": f"Update student {id}"})

    def patch(self, id):
        return jsonify({"message": f"Partial update student {id}"})

    def delete(self, id):
        return jsonify({"message": f"Delete student {id}"})


class Drives(Resource):
    def get(self):
        return jsonify({"message": "List drives endpoint"})

    def post(self):
        return jsonify({"message": "Create drive endpoint"})


class Drive(Resource):
    def get(self, id):
        return jsonify({"message": f"Get drive {id}"})

    def put(self, id):
        return jsonify({"message": f"Update drive {id}"})

    def patch(self, id):
        return jsonify({"message": f"Partial update drive {id}"})

    def delete(self, id):
        return jsonify({"message": f"Delete drive {id}"})


class Vaccinations(Resource):
    def get(self):
        return jsonify({"message": "List vaccinations endpoint"})

    def post(self):
        return jsonify({"message": "Create vaccination endpoint"})


class Vaccination(Resource):
    def get(self, id):
        return jsonify({"message": f"Get vaccination {id}"})

    def put(self, id):
        return jsonify({"message": f"Update vaccination {id}"})

    def delete(self, id):
        return jsonify({"message": f"Delete vaccination {id}"})


class StudentVaccinations(Resource):
    def post(self, studentId):
        return jsonify({"message": f"Create vaccination for student {studentId}"})


class ReportsVaccinations(Resource):
    def get(self):
        return jsonify({"message": "List vaccination reports"})


class ReportsExport(Resource):
    def get(self):
        return jsonify({"message": "Export reports endpoint"})


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
