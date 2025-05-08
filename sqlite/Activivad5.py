import sqlite3
from DataBaseManager import DataBaseManager

dataBaseManager = DataBaseManager()

con = sqlite3.connect(dataBaseManager.database)
materia = (11,'Cultura digital', 'Gomez Fernandez Luis Leonardo', 8)
dataBaseManager.create_materia(con, materia)

cur = con.cursor()
cur.execute("Select * from materias;")
table_list = cur.fetchall()
for row in table_list:
    print(row)
con.close()