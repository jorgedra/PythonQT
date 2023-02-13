from PySide6.QtWidgets import QApplication, QMainWindow, QDial, QLabel, QLineEdit, QDateTimeEdit, QSlider, QComboBox 


class Ventana(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Ejercicio2")
        self.setFixedSize(350, 250)

        # Labels
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)
        self.label1.move(50, 0)
        self.label2.move(150, 0)
        self.label3.move(0, 100)
        self.label4.move(270, 50)
        self.label5.move(110, 150)


        # QLineEdit
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setFixedSize(50, 30)
        self.lineEdit.move(100, 0)
        self.lineEdit.textChanged[str].connect(self.onChanged)

        # Dial
        self.dial = QDial(self)
        self.dial.setRange(0, 5)
        self.dial.setFixedSize(50, 30)
        self.dial.valueChanged.connect(self.dialCambiado)
        self.dialCambiado(self.dial.value())

        # DataTime
        self.data = QDateTimeEdit(self)
        self.data.move(0, 50)
        self.data.setFixedSize(140, 40)
        self.data.dateTimeChanged.connect(self.GetDatetime)

        # Slider
        self.slider = QSlider(self)
        self.slider.setPageStep(1)
        self.slider.move(150, 50)
        self.slider.setRange(0, 5)
        self.slider.valueChanged.connect(self.SliderChange)

        # ComboBox
        self.combo = QComboBox(self)
        self.combo.move(0,150)
        self.combo.addItems(["Pepe","Manolo","Luis","Knekro","Marillas"])
        self.combo.currentTextChanged.connect(self.comboCambiado)



    # Funciones
    def dialCambiado(self, value):
        self.label1.setText(str(value))

    def onChanged(self, text):
        self.label2.setText(text)

    def GetDatetime(self):
        datos = self.data.dateTime()
        datos_string = datos.toString(self.data.displayFormat())
        self.label3.setText(datos_string)

    def SliderChange(self, value):
        self.label4.setText(str(value))

    def comboCambiado(self,value):
        self.label5.setText(value)


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()
