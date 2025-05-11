from flask import jsonify
from flask_restful_swagger_3 import swagger, Resource

from app.db import get_db


class Dashboard(Resource):
    @staticmethod
    @swagger.tags(['Dashboard'])
    @swagger.response(response_code=200, description='Return vaccination stats',
                      schema={'type': 'object',
                              'properties': {
                                  'totalStudents': {'type': 'integer'},
                                  'vaccinatedStudents': {'type': 'integer'},
                                  'unvaccinatedStudents': {'type': 'integer'}
                              }
                              })
    def get():
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM students')
        total_students = cur.fetchone()[0]
        cur.execute('SELECT COUNT(DISTINCT student_id) FROM student_vaccines')
        vaccinated_students = cur.fetchone()[0]
        unvaccinated_students = total_students - vaccinated_students
        cur.close()
        return jsonify({
            "totalStudents": total_students,
            "vaccinatedStudents": vaccinated_students,
            "unvaccinatedStudents": unvaccinated_students
        })
