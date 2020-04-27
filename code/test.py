import psycopg2

connection = psycopg2.connect(database="bmm", host="bmm-real.cqk0ag5bavpf.ap-southeast-1.rds.amazonaws.com", user="RexWar", password="Cibreonline70")
cursor = connection.cursor()
cursor.execute("SELECT * FROM spareparts ORDER BY id")
results = cursor.fetchall()
print(results)
connection.close()