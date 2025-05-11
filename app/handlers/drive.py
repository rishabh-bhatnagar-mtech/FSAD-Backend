from flask import jsonify, request, make_response
from flask_restful import Resource

from app.db import get_db


class Drives(Resource):
    @staticmethod
    def get():
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
                    SELECT id, name, date, doses_available, applicable_classes, vaccine_name
                    FROM drives
                    ORDER BY id
                    """)
        drives = []
        for row in cur.fetchall():
            drives.append({
                "id": row[0],
                "name": row[1],
                "date": row[2].isoformat() if row[2] else None,
                "doses_available": row[3],
                "vaccine_name": row[5],
                "applicable_classes": [cls.strip() for cls in row[4].split(',')] if row[4] else []
            })
        cur.close()
        return jsonify(drives)

    @staticmethod
    def post():
        conn = get_db()
        cur = conn.cursor()
        data = request.get_json()
        try:
            cur.execute(
                "INSERT INTO drives (id, name, date, doses_available, applicable_classes, vaccine_name) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    data.get("id"),
                    data.get("name"),
                    data.get("date"),
                    int(data.get("doses_available")),
                    data.get("applicable_classes"),
                    data.get("vaccine_name")
                )
            )
            conn.commit()
            cur.close()
            return make_response(jsonify({"message": "Drive created", "id": data.get("id")}), 201)
        except Exception as e:
            conn.rollback()
            cur.close()
            return make_response(jsonify({"error": str(e)}), 400)


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
