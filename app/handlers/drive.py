from flask import request
from flask_restx import Namespace, Resource, fields
from app.db import get_db

api = Namespace('Drives', description='Drive management')

drive_model = api.model('Drive', {
    'id': fields.String(required=True, description='Drive ID'),
    'name': fields.String(required=True, description='Drive name'),
    'date': fields.String(required=True, description='Date (YYYY-MM-DD)'),
    'doses_available': fields.Integer(required=True, description='Number of doses available'),
    'vaccine_name': fields.String(required=True, description='Vaccine name'),
    'applicable_classes': fields.List(fields.String, required=True, description='Applicable classes'),
})

@api.route('')
class Drives(Resource):
    @api.marshal_list_with(drive_model)
    def get(self):
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
        return drives, 200

    @api.expect(drive_model)
    @api.response(201, 'Drive created')
    @api.response(400, 'Validation Error')
    def post(self):
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
                    ','.join(data.get("applicable_classes")) if isinstance(data.get("applicable_classes"), list) else data.get("applicable_classes"),
                    data.get("vaccine_name")
                )
            )
            conn.commit()
            cur.close()
            return {"message": "Drive created", "id": data.get("id")}, 201
        except Exception as e:
            conn.rollback()
            cur.close()
            return {"error": str(e)}, 400
