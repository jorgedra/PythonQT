from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton,QVBoxLayout
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout horizontal")

        # Creamos un objeto layout horizontal
        layout_padre = QHBoxLayout()
        layout_hijo1 = QVBoxLayout()
        layout_hijo2 = QHBoxLayout()

        # Añadimos los layouts al padre
        layout_padre.addLayout(layout_hijo1)
        layout_padre.addLayout(layout_hijo2)

        # Creamos un componente principal para la ventana
        componente_principal = QWidget()
        # Le assignamos el layout vertical como disposición
        componente_principal.setLayout(layout_padre)
        self.setCentralWidget(componente_principal)

        layout_hijo1.addWidget(QPushButton('V1'))
        layout_hijo1.addWidget(QPushButton('V2'))
        layout_hijo1.addWidget(QPushButton('V3'))
        layout_hijo1.addWidget(QPushButton('V4'))

        layout_hijo2.addWidget(QPushButton('H1'))
        layout_hijo2.addWidget(QPushButton('H2'))
        layout_hijo2.addWidget(QPushButton('H3'))
        layout_hijo2.addWidget(QPushButton('H4'))




app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()

