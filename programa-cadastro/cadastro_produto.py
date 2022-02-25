from PyQt5 import uic, QtWidgets 
import mysql.connector
import time 

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database="cadastro_produtos"
) #conexao com o bd de dados do MySQL criado.
data_hora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# estamos pegando a data e hora atual para utilizar como data da criacao do registro no banco.

def funcao_principal():
    cod = formulario.lineEdit.text().title().strip()
    desc = formulario.lineEdit_2.text().title().strip()
    preco = formulario.lineEdit_3.text().strip()
    
    categoria = ''
    
    if formulario.radioButton.isChecked():
        print("A categoria Vestuário foi selecionada!")
        categoria = 'Vestuário'
    elif formulario.radioButton_2.isChecked():
        print("A categoria Acessórios foi selecionada!")
        categoria = 'Acessórios'
    elif formulario.radioButton_3.isChecked():
        print("A categoria Outros foi selecionada!")
        categoria = 'Outros'
    else:
        print("Favor selecionar a categoria!")
            
    print("Código: " + cod)
    print('Descrição: ', desc)
    print("Preço: ", preco)
    print("Os dados foram inseridos no banco de dados!")
    
    cursor = banco.cursor()  
    comando_sql = 'INSERT INTO produtos (codigo, descricao, preco, categoria, data) VALUES (%s,%s,%s,%s,%s)'
    dados = (str(cod), str(desc), str(preco), categoria, str(data_hora))
    cursor.execute(comando_sql, dados) # o cursor precisa de dois parâmetros, um o comando e outro o tipo de dados.
    banco.commit()

app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui") #passando o arquivo que contém o layout do programa
formulario.pushButton.clicked.connect(funcao_principal) #nome pushbuttom descoberto dentro do program qt

formulario.show()
app.exec()