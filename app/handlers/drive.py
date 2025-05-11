from flask import jsonify
from flask_restful import Resource

from app.db import get_db


class Drives(Resource):
    @staticmethod
    def get():
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
                    SELECT id, name, date, doses_available, applicable_classes
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
                "applicable_classes": [cls.strip() for cls in row[4].split(',')] if row[4] else []
            })
        cur.close()
        return jsonify(drives)

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
