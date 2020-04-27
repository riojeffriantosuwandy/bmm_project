from flask_restful import Resource
import psycopg2

class Spareparts(Resource):
    def get(self):
        connection = psycopg2.connect(database="bmm", host="bmm-real.cqk0ag5bavpf.ap-southeast-1.rds.amazonaws.com", user="RexWar", password="Cibreonline70")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM spareparts ORDER BY id")
        results = cursor.fetchall()
        connection.close()
        return {"Spareparts": [{"Spareparts name": x[1], "PN": x[3]} for x in results]}
