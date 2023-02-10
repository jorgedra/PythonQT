# Importamos las librerías de PyQt que vamos a utilizar
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QLabel
from PyQt5.QtCore import Qt


# Creamos una clase que hereda de QWidget para nuestra ventana principal
class VelocimeterWindow(QWidget):
    def __init__(self):
        # Inicializamos la ventana y establecemos su título y tamaño
        super().__init__()
        self.setWindowTitle("Velocímetro")
        self.setFixedSize(250, 150)

        # Creamos un dial y lo agregamos a la ventana
        self.dial = QDial(self)
        self.dial.setNotchesVisible(True)
        self.dial.setWrapping(True)
        self.dial.setMinimum(0)
        self.dial.setMaximum(200)
        self.dial.setValue(0)
        self.dial.setFixedSize(100, 100)
        self.dial.move(75, 25)

        # Creamos una etiqueta y la agregamos a la ventana
        self.label = QLabel("0 km/h",self)
        self.label.move(105, 7)
        self.label.resize(60,10)

        # Conectamos la señal valueChanged del dial a una función que actualizará la etiqueta
        self.dial.valueChanged.connect(self.updateLabel)

    def updateLabel(self):
        # Actualizamos el texto de la etiqueta con el valor del dial
        self.label.setText("{} km/h".format(self.dial.value()))

# Creamos una instancia de nuestra clase y la mostramos en pantalla
app = QApplication([])
window = VelocimeterWindow()
window.show()
app.exec()
