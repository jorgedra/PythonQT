from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Ejercicio2")
        self.label1 = QLabel(self)
        self.line1 = QLineEdit(self)
        self.line1.textChanged[str].connect(self.onChanged)
        self.line1.setMaxLength(5)
        self.line1.setFixedSize(50,30)
        self.line1.move(50,0)

    def onChanged(self,text):
        self.label1.setText(text)

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()
