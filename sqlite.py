import sqlite3

banco = sqlite3.connect("Banco_dados.db")

cursor = banco.cursor()

cursor.execute("CREATE TABLE People(nome text, idade integer, telefone integer)")

cursor.execute("INSERT INTO People VALUES('Geovano', 29, 91983298535)")

banco.commit()

#cursor.execute("SELECT * FROM People")
#print(cursor.fetchall())

#--update--
import sqlite3
banco = sqlite3.connect('bancodata.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE registros (link_site text, link_img text, titulo text, resumo text)")
cursor.execute("INSERT INTO registros VALUES('https://linkteste.org/dl/','testando.com/img-teste-prog-1','titulo1','resumo1 lalalala')")
banco.commit()
#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())
