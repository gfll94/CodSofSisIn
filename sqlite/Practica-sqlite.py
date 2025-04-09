import sqlite3

db_file = 'C:/Users/Docente1/Contenido/CodSofSis/Parcial2/sqlite/testing.db'
con = sqlite3.connect(db_file)
cur = con.cursor()
cur.execute("Select * from materias;")
table_list = cur.fetchall()
for row in table_list:
    print(row[0])
con.close()