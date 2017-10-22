import sqlite3
conn = sqlite3.connect("E:\软件\djangowork\db.sqlite3")
conn.text_factory = str
cursor = conn.cursor()
cursor.execute("select * from app_pachong7")
m=cursor.fetchall()
print(m)