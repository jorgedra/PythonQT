from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QMessageBox


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana con dos botones')
        self.resize(300, 200)
        self.move(200, 100)

        self.button1 = QPushButton('Sí', self)
        self.button1.move(50, 50)
        self.button1.clicked.connect(self.on_button1_clicked)

        self.button2 = QPushButton('No', self)
        self.button2.move(150, 50)
        self.button2.clicked.connect(self.on_button2_clicked)

    def on_button1_clicked(self):
        QMessageBox.information(self, 'Mensaje', 'Has pulsado el botón Sí')

    def on_button2_clicked(self):
        QMessageBox.information(self, 'Mensaje', 'Has pulsado el botón No')


app = QApplication([])
window = MyWindow()
window.show()
app.exec()