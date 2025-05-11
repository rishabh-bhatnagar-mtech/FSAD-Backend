from flask import jsonify, request, make_response
from flask_restful import Resource

from app.db import get_db  # you should define this to return a psycopg2 connection


class Students(Resource):
    @staticmethod
    def get():
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
        return jsonify(students)

    @staticmethod
    def post():
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
            return jsonify({"message": "Students created", "ids": created_ids})
        except Exception as e:
            conn.rollback()
            cur.close()
            return jsonify({"error": str(e)}), 400


class Student(Resource):
    @staticmethod
    def put(student_id):
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
            return make_response(jsonify({"message": "Student updated", "id": student_id}))
        except Exception as e:
            conn.rollback()
            cur.close()
            return make_response(jsonify({"error": str(e)}), 400)
