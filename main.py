from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui

def RegisterScreen():
    login.close()
    register.show()

#def NewRegister():
   # usuario = tel_Cad.lineEdit_10.text()
   # nome = tel_Cad.lineEdit.text()
   # cpf = tel_Cad.lineEdit_2.text()
   # senha = tel_Cad.lineEdit_8.text()
   # c_senha = tel_Cad.lineEdit_9.text()
    #diaPg = tel_Cad.lineEdit_11.text()

    #if (senha == c_senha and usuario != "" and nome != "" and cpf != ""  and diaPg != ""):
       # try:
         #   cursor = banco.cursor()
          #  cursor.execute(
             #   "INSERT INTO clientes VALUES ('" + usuario + "','" + nome + "','" + cpf + "','" + senha + "','" + diaPg + "')")
          #  banco.commit()
         #   banco.close()

       # except mysql as erro:
         #   print("erro ao inserir dados no banco")

   # else:
      #  tel_Cad.label_5.setText("Dados incompletos ou senhas não conferem")


def LoginScreen():
    user = login.lineEdit.text()
    passw = login.lineEdit_2.text()

    if user == "zackcmariano" and passw == "1234":
        login.close()
        logged.show()
    else:
        login.label_3.setText("Dados de Login Incorretos")

def CloseScreen():
    logged.close()


#READING THE UI FILES#
app=QtWidgets.QApplication([])
login=uic.loadUi("login.ui")
register=uic.loadUi("newregister.ui")
logged=uic.loadUi("logged.ui")
login.pushButton.clicked.connect(LoginScreen)
login.pushButton_2.clicked.connect(RegisterScreen)
logged.pushButton.clicked.connect(CloseScreen)

#INSERT IMAGE#
icon=QtGui.QPixmap([])
login.label_4.setPixmap(QtGui.QPixmap('logo.png'))


login.show()
app.exec()
