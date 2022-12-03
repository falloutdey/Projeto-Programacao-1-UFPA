import sqlite3

banco = sqlite3.connect('bancodata.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE registros (link_site text, link_img text, titulo text, resumo text)")

cursor.execute("INSERT INTO registros VALUES('https://linkteste.org/dl/','testando.com/img-teste-prog-1','titulo1','resumo1 lalalala')")

banco.commit()

#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())
