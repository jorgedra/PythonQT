from PySide6.QtWidgets import QApplication, QLabel, QWidget
class Ventana(QWidget):
    def __init__(self):

        super().__init__()

        self.setWindowTitle("Ventana")

        self.etiqueta1 = QLabel("HOLA MONDONGO", self)
if __name__ == "__main__":

    app = QApplication([])

    ventana1 = Ventana()

    ventana1.show()

    app.exec()
