from PySide6.QtWidgets import QApplication, QMainWindow,QLabel,QComboBox 

class Ventana(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Ejercicio2")
        self.setFixedSize(250, 150)

        # Labels
        self.label1 = QLabel(self)
        self.label1.move(0, 50)
        self.label1.setMinimumWidth(100000)


        # ComboBox
        self.combo = QComboBox(self)
        self.combo.move(0,0)
        self.combo.addItems(["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        self.combo.currentIndexChanged.connect(self.comboNumero)

        self.label1.setText(self.combo.currentText() + " es el mes numero " + str(self.combo.currentIndex() + 1))
        print(self.combo.currentText() + " es el mes numero " + str(self.combo.currentIndex() + 1))

    def comboNumero(self,value):
        numeroCb = self.combo.currentIndex()
        textoCb = self.combo.currentText()
        self.label1.setText(textoCb + " es el mes numero " + str(numeroCb + 1))
        print(textoCb + " es el mes numero " + str(numeroCb + 1))


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()
