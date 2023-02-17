from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton
    ,QLabel, QLineEdit, QGridLayout, QStackedLayout,QHBoxLayout
)




class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout vertical")

        layout_principal = QHBoxLayout()
        # Creamos un objeto layout vertical
        self.lblName = QLabel("Nombre:")
        self.txtName = QLineEdit()
        self.txtName.setPlaceholderText("Nombre de usuario")
        self.lblCheck = QLabel(self)
        self.mensaje = QLabel()
        self.mensaje.setHidden(True)

        self.lblPass = QLabel("Contraseña:")
        self.txtPass = QLineEdit(self)
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.txtPass.setPlaceholderText("Contraseña de usuario")
        self.irLogin = QPushButton("Ir a login")
        self.irRegistro = QPushButton("Ir a registro")


        self.lblName2 = QLabel("Nombre:")
        self.txtName2 = QLineEdit()
        self.txtName2.setPlaceholderText("Nombre de usuario")
        self.lblCheck2 = QLabel(self)

        self.lblPass2 = QLabel("Contraseña:")
        self.txtPass2 = QLineEdit(self)
        self.txtPass2.setEchoMode(QLineEdit.Password)
        self.txtPass2.setPlaceholderText("Contraseña de usuario")

        self.stack = QStackedLayout()
        self.grid = QGridLayout()
        self.grid2 = QGridLayout()
        self.lBotones = QGridLayout()
        self.grid.addWidget(self.lblName, 0, 0)
        self.grid.addWidget(self.txtName, 0, 1)
        self.grid.addWidget(self.lblPass, 1, 0)
        self.grid.addWidget(self.txtPass, 1, 1)
        self.grid.addWidget(self.mensaje, 3, 0)
        self.lBotones.addWidget(self.irLogin, 1, 2)
        self.lBotones.addWidget(self.irRegistro, 0, 2)

        self.grid2.addWidget(self.lblName2, 0, 0)
        self.grid2.addWidget(self.txtName2, 0, 1)
        self.grid2.addWidget(self.lblPass2, 1, 0)
        self.grid2.addWidget(self.txtPass2, 1, 1)

        layour_login = QWidget()
        layour_login.setLayout(self.grid)

        layout_registro = QWidget()
        layout_registro.setLayout(self.grid2)

        self.stack.addWidget(layout_registro)
        self.stack.addWidget(layour_login)

        self.btnLogin = QPushButton("Login", self)
        self.btnRegistrarse = QPushButton("Registrarse",self)
        self.grid.addWidget(self.btnLogin, 2, 0, 1, 2)
        self.grid2.addWidget(self.btnRegistrarse, 2, 0, 1, 2)


        self.btnLogin.clicked.connect(self.login)
        self.btnRegistrarse.clicked.connect(self.registro)
        self.irLogin.clicked.connect(self.irALogin)
        self.irRegistro.clicked.connect(self.irARegistro)
        # Creamos un componente principal para la ventana
        componente_principal = QWidget()
        # Le assignamos el layout vertical como disposición
        componente_principal.setLayout(layout_principal)
        self.setCentralWidget(componente_principal)

        layout_principal.addLayout(self.stack)
        layout_principal.addLayout(self.lBotones)


    def login(self):
        User = self.usuario
        Pass = self.contraseña
        if (User == self.txtName.text() and Pass == self.txtPass.text()):
            self.mensaje.setText("<font color='green'>Correcto</font>")
            self.mensaje.setHidden(False)
        elif (User != self.txtName.text() or Pass != self.txtPass.text()):
            self.mensaje.setText("<font color='red'>Incorrecto</font>")
            self.mensaje.setHidden(False)

    def registro(self):
        self.usuario = self.txtName2.text()
        self.contraseña = self.txtPass2.text()
        self.stack.setCurrentIndex(1)

    def irARegistro(self):
        self.stack.setCurrentIndex(0)

    def irALogin(self):
        self.stack.setCurrentIndex(1)


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()
