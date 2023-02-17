from PySide6.QtWidgets import *


class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(450, 350)
        layout_principal = QHBoxLayout()
        layout_grid = QGridLayout()

        componente_principal = QWidget()

        componente_principal.setLayout(layout_principal)
        self.setCentralWidget(componente_principal)

        layout_principal.addLayout(layout_grid)

        self.botonH = QPushButton("Historial")
        self.lbNumeros = QLabel()
        self.bt1 = QPushButton("1")
        self.bt2 = QPushButton("2")
        self.bt3 = QPushButton("3")
        self.bt4 = QPushButton("4")
        self.bt5 = QPushButton("5")
        self.bt6 = QPushButton("6")
        self.bt7 = QPushButton("7")
        self.bt8 = QPushButton("8")
        self.bt9 = QPushButton("9")
        self.bt0 = QPushButton("0")
        self.btIgual = QPushButton("=")
        self.btResta = QPushButton("-")
        self.btSuma = QPushButton("+")
        self.btClean = QPushButton("CE")
        self.btDivision = QPushButton("/")
        self.btMultiplicacion = QPushButton("*")


        layout_grid.addWidget(self.botonH, 0, 0, 1, 4)
        layout_grid.addWidget(self.lbNumeros, 1, 0, 1, 4)
        layout_grid.addWidget(self.bt7, 2, 0)
        layout_grid.addWidget(self.bt8, 2, 1)
        layout_grid.addWidget(self.bt9, 2, 2)
        layout_grid.addWidget(self.btClean, 2, 3)
        layout_grid.addWidget(self.bt4, 3, 0)
        layout_grid.addWidget(self.bt5, 3, 1)
        layout_grid.addWidget(self.bt6, 3, 2)
        layout_grid.addWidget(self.btDivision, 3, 3)
        layout_grid.addWidget(self.bt1, 4, 0)
        layout_grid.addWidget(self.bt2, 4, 1)
        layout_grid.addWidget(self.bt3, 4, 2)
        layout_grid.addWidget(self.btMultiplicacion, 4, 3)
        layout_grid.addWidget(self.bt0, 5, 0)
        layout_grid.addWidget(self.btIgual, 5, 1)
        layout_grid.addWidget(self.btResta, 5, 2)
        layout_grid.addWidget(self.btSuma, 5, 3)


        self.bt0.clicked.connect(self.boton0)
        self.bt1.clicked.connect(self.boton1)
        self.bt2.clicked.connect(self.boton2)
        self.bt3.clicked.connect(self.boton3)
        self.bt4.clicked.connect(self.boton4)
        self.bt5.clicked.connect(self.boton5)
        self.bt6.clicked.connect(self.boton6)
        self.bt7.clicked.connect(self.boton7)
        self.bt8.clicked.connect(self.boton8)
        self.bt9.clicked.connect(self.boton9)
        self.btClean.clicked.connect(self.limpiar)

    
    def boton0(self):
        valorBoton = self.bt0.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)   

    def boton1(self):
        valorBoton = self.bt1.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)

    def boton2(self):
        valorBoton = self.bt2.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)

    def boton3(self):
        valorBoton = self.bt3.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)
    
    def boton4(self):
        valorBoton = self.bt4.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)

    def boton5(self):
        valorBoton = self.bt5.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)

    def boton6(self):
        valorBoton = self.bt6.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)

    def boton7(self):
        valorBoton = self.bt7.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)

    def boton8(self):
        valorBoton = self.bt8.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)
        
    def boton9(self):
        valorBoton = self.bt9.text()
        self.lbNumeros.setText(self.lbNumeros.text() + valorBoton)
    
    def limpiar(self):
        self.lbNumeros.setText("")



if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()
