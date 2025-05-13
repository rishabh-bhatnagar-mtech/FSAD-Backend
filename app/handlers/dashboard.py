from flask_restx import Namespace, Resource, fields
from app.db import get_db

api = Namespace('dashboard', description='Dashboard operations')

dashboard_stats = api.model('DashboardStats', {
    'totalStudents': fields.Integer,
    'vaccinatedStudents': fields.Integer,
    'unvaccinatedStudents': fields.Integer,
})

@api.route('/stats')
class Dashboard(Resource):
    @api.marshal_with(dashboard_stats)
    def get(self):
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM students')
        total_students = cur.fetchone()[0]
        cur.execute('SELECT COUNT(DISTINCT student_id) FROM student_vaccines')
        vaccinated_students = cur.fetchone()[0]
        unvaccinated_students = total_students - vaccinated_students
        cur.close()
        return {
            "totalStudents": total_students,
            "vaccinatedStudents": vaccinated_students,
            "unvaccinatedStudents": unvaccinated_students
        }
