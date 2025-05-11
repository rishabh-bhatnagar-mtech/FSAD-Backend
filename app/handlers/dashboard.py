from flask import jsonify
from flask_restful import Resource

from app.db import get_db


class Dashboard(Resource):
    @staticmethod
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
