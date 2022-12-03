import sqlite3

banco = sqlite3.connect('bancodata.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE registros (link_site text, link_img text, titulo text, resumo text)")

cursor.execute("INSERT INTO registros VALUES('https://linkteste.org/dl/','testando.com/img-teste-prog-1','titulo1','resumo1 lalalala')")

banco.commit()

#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())

#--adicionando ao banco de dados com variaveis--

import sqlite3
linksite = 'https://ewiedihjf.org/dl/'
linkimg = 'testando.com/qualquercoisa-teste/'
titulo = 'titulo_variavel'
resumo = 'iwjdqio dhwuiqdh dhwuiqedhiqwhud'

banco = sqlite3.connect('bancodata.db')
cursor = banco.cursor()
cursor.execute("INSERT INTO registros VALUES('"+linksite+"','"+linkimg+"','"+titulo+"','"+resumo+"')")
banco.commit()
