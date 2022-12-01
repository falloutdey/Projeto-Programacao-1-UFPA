import sqlite3

banco = sqlite3.connect("Banco_dados.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE People(nome text, idade integer, telefone integer)")

cursor.execute("INSERT INTO People VALUES('Geovano', 29, 91983298535)")

banco.commit

#cursor.execute("SELECT * FROM People")
#print(cursor.fetchall())

