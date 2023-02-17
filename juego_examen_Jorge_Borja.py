from PySide6.QtWidgets import *


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cuanto sabes")
        self.setFixedWidth(450)
        layout_principal = QHBoxLayout()

        self.stack = QStackedLayout()
        self.gridUser = QGridLayout()
        self.LyerrorEdad = QHBoxLayout()
        self.gridJuego1 = QGridLayout()
        self.gridJuego2 = QGridLayout()
        self.LyFin = QHBoxLayout()

        self.lbUser = QLabel("Usuario o correo:")
        self.txtUser = QLineEdit()
        self.lblerror = QLabel("Introduce un correo")
        self.lblerror.setHidden(True)
        self.lbFecha = QLabel("Fecha de nacimiento")
        self.fechaN = QDateEdit()
        self.btJugar = QPushButton("Registrar y jugar!!")
        self.lbError = QLabel("No tienes la edad suficiente")
        self.lbPregunta1 = QLabel("Pregunta1: ¿Cual es la capital de Francia?")
        self.btC1 = QPushButton("Sevilla")
        self.btC2 = QPushButton("Paris")
        self.btC3 = QPushButton("Oporto")
        self.btC4 = QPushButton("Amsterdam")
        self.lbErrorJuego1 = QLabel(
            "<font color='red'>Respuesta incorrecta</font>")
        self.lbPregunta2 = QLabel("Pregunta2: Resuelve el reto")
        self.slider1 = QSlider()
        self.slider2 = QSlider()
        self.slider3 = QSlider()
        self.btResuelve = QPushButton("Resuelve")
        self.lbFinal = QLabel("<font color='green'>HAS GANADO</font>")

        self.gridUser.addWidget(self.lbUser, 0, 0, 1, 2)
        self.gridUser.addWidget(self.txtUser, 0, 1, 1, 2)
        self.gridUser.addWidget(self.lbFecha, 1, 0, 1, 2)
        self.gridUser.addWidget(self.fechaN, 1, 1, 1, 2)
        self.gridUser.addWidget(self.lblerror, 1, 1, 2, 2)
        self.gridUser.addWidget(self.btJugar, 2, 0, 1, 3)

        self.gridJuego1.addWidget(self.lbPregunta1, 0, 0, 1, 4)
        self.gridJuego1.addWidget(self.btC1, 1, 0, 1, 2)
        self.gridJuego1.addWidget(self.btC2, 1, 2, 1, 2)
        self.gridJuego1.addWidget(self.btC3, 2, 0, 1, 2)
        self.gridJuego1.addWidget(self.btC4, 2, 2, 1, 2)
        self.gridJuego1.addWidget(self.lbErrorJuego1, 3, 0)
        self.lbErrorJuego1.setHidden(True)

        self.gridJuego2.addWidget(self.lbPregunta2, 0, 0, 1, 4)
        self.gridJuego2.addWidget(self.slider1, 1, 0)
        self.gridJuego2.addWidget(self.slider2, 1, 1)
        self.gridJuego2.addWidget(self.slider3, 1, 2)
        self.gridJuego2.addWidget(self.btResuelve, 1, 3, 1, 2)

        self.LyerrorEdad.addWidget(self.lbError)

        self.LyFin.addWidget(self.lbFinal)

        self.btJugar.clicked.connect(self.avanzar1)
        self.btC1.clicked.connect(self.fallo)
        self.btC3.clicked.connect(self.fallo)
        self.btC4.clicked.connect(self.fallo)
        self.btC2.clicked.connect(self.avanzar2)
        self.btResuelve.clicked.connect(self.avanzarFin)

        layour_login = QWidget()
        layour_login.setLayout(self.gridUser)

        layour_error = QWidget()
        layour_error.setLayout(self.LyerrorEdad)

        layout_juego1 = QWidget()
        layout_juego1.setLayout(self.gridJuego1)

        layout_juego2 = QWidget()
        layout_juego2.setLayout(self.gridJuego2)

        layout_fin = QWidget()
        layout_fin.setLayout(self.LyFin)

        self.stack.addWidget(layour_login)
        self.stack.addWidget(layour_error)
        self.stack.addWidget(layout_juego1)
        self.stack.addWidget(layout_juego2)
        self.stack.addWidget(layout_fin)

        componente_principal = QWidget()

        componente_principal.setLayout(layout_principal)
        self.setCentralWidget(componente_principal)

        layout_principal.addLayout(self.stack)

    def avanzar1(self):
        datos = self.fechaN.dateTime().date().year()
        if not (self.txtUser.text() == ""):
            self.lblerror.setHidden(True)
            if (2022 - datos < 18):
                self.stack.setCurrentIndex(1)
            else:
                self.stack.setCurrentIndex(2)
        else:
            self.lblerror.setHidden(False)

    def fallo(self):
        self.lbErrorJuego1.setHidden(False)

    def avanzar2(self):
        self.stack.setCurrentIndex(3)

    def avanzarFin(self):
        if (self.slider1.value() == self.slider2.value() and self.slider1.value() == self.slider3.value()):
            self.stack.setCurrentIndex(4)


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
