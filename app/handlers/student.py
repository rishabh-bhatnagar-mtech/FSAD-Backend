from flask import request
from flask_restx import Namespace, Resource, fields

from app.db import get_db

api = Namespace('Students', description='Student management')

vaccine_model = api.model('Vaccine', {
    'name': fields.String(required=True, description='Vaccine name'),
    'driveId': fields.String(required=True, description='Drive ID'),
})

student_model = api.model('Student', {
    'id': fields.String(required=True, description='Student ID'),
    'name': fields.String(required=True, description='Student name'),
    'class': fields.String(required=True, description='Class'),
    'vaccines': fields.List(fields.Nested(vaccine_model), description='List of vaccines')
})


@api.route('')
class Students(Resource):
    @api.marshal_list_with(student_model)
    def get(self):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
                    SELECT s.id,
                           s.name,
                           s.class,
                           COALESCE(json_agg(json_build_object('name', v.name, 'driveId', sv.drive_id))
                                    FILTER (WHERE v.name IS NOT NULL), '[]') AS vaccines
                    FROM students s
                             LEFT JOIN student_vaccines sv ON s.id = sv.student_id
                             LEFT JOIN vaccines v ON sv.vaccine_id = v.id
                    GROUP BY s.id, s.name, s.class
                    ORDER BY s.id
                    """)
        students = []
        for row in cur.fetchall():
            students.append({
                "id": row[0],
                "name": row[1],
                "class": row[2],
                "vaccines": row[3]
            })
        cur.close()
        return students, 200

    @api.expect([student_model])
    @api.response(201, 'Students created')
    @api.response(400, 'Validation Error')
    def post(self):
        conn = get_db()
        cur = conn.cursor()
        data = request.get_json()
        if isinstance(data, dict):
            data = [data]
        created_ids = []
        try:
            for entry in data:
                cur.execute(
                    "INSERT INTO students (id, name, class) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING",
                    (entry.get("id"), entry.get("name"), entry.get("class"))
                )
                for v in entry.get("vaccines", []):
                    cur.execute("SELECT id FROM vaccines WHERE name=%s", (v["name"],))
                    vaccine_row = cur.fetchone()
                    if vaccine_row:
                        vaccine_id = vaccine_row[0]
                    else:
                        cur.execute("INSERT INTO vaccines (name) VALUES (%s) RETURNING id", (v["name"],))
                        vaccine_id = cur.fetchone()[0]
                    cur.execute(
                        "INSERT INTO student_vaccines (student_id, vaccine_id, drive_id) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                        (entry.get("id"), vaccine_id, v["driveId"])
                    )
                created_ids.append(entry.get("id"))
            conn.commit()
            cur.close()
            return {"message": "Students created", "ids": created_ids}, 201
        except Exception as e:
            conn.rollback()
            cur.close()
            return {"error": str(e)}, 400


@api.route('/<string:student_id>')
class Student(Resource):
    @api.expect(student_model)
    @api.response(200, 'Student updated')
    @api.response(400, 'Validation Error')
    def put(self, student_id):
        conn = get_db()
        cur = conn.cursor()
        data = request.get_json()
        try:
            cur.execute(
                "UPDATE students SET name=%s, class=%s WHERE id=%s",
                (data.get("name"), data.get("class"), student_id)
            )
            cur.execute("DELETE FROM student_vaccines WHERE student_id=%s", (student_id,))
            for v in data.get("vaccines", []):
                cur.execute("SELECT id FROM vaccines WHERE name=%s", (v["name"],))
                vaccine_row = cur.fetchone()
                if vaccine_row:
                    vaccine_id = vaccine_row[0]
                else:
                    cur.execute("INSERT INTO vaccines (name) VALUES (%s) RETURNING id", (v["name"],))
                    vaccine_id = cur.fetchone()[0]
                cur.execute(
                    "INSERT INTO student_vaccines (student_id, vaccine_id, drive_id) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                    (student_id, vaccine_id, v["driveId"])
                )
            conn.commit()
            cur.close()
            return {"message": "Student updated", "id": student_id}, 200
        except Exception as e:
            conn.rollback()
            cur.close()
            return {"error": str(e)}, 400
