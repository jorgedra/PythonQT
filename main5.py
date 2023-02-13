import os
import platform

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import *


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "Ponte aprueba 4")
        self.setGeometry(600,600,500,300)
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        ruta_icono1 = os.path.join(r"C:\Users\JorgeDAM2\Desktop\Proyecto1\imgs" , "carpeta.png")
        ruta_icono2 = os.path.join(r"C:\Users\JorgeDAM2\Desktop\Proyecto1\imgs" , "guardar.png")
        ruta_icono3 = os.path.join(r"C:\Users\JorgeDAM2\Desktop\Proyecto1\imgs" , "salir.png")

        self.accion = QAction(QIcon(ruta_icono1), "Abrir archivo", self)
        self.accion.setStatusTip("Abrir archivo")
        self.accion.setShortcut(QKeySequence("Ctrl+o"))
        self.accion.triggered.connect(self.abrir_archivo)

        self.accion2 = QAction(QIcon(ruta_icono2), "Guardar archivo", self)
        self.accion2.setStatusTip("Guardar archivo")
        self.accion2.setShortcut(QKeySequence("Ctrl+s"))
        self.accion2.triggered.connect(self.guardar_archivo)

        self.accion3 = QAction(QIcon(ruta_icono3), "Salir", self)
        self.accion3.setStatusTip("Salir")
        self.accion3.setShortcut(QKeySequence("Ctrl+q"))
        self.accion3.triggered.connect(self.salir)

        menu.addAction(self.accion)
        menu.addAction(self.accion2)
        menu.addAction(self.accion3)

        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(self.accion)
        barra_herramientas.addAction(self.accion2)
        barra_herramientas.addAction(self.accion3)
        self.addToolBar(barra_herramientas)

        barra_estado = self.statusBar()
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        barra_estado.showMessage("Listo. Esperando acción ...", 3000)

        # Creamos un componente flotante
        dock1 = QDockWidget()
        # Agregamos título a este componente
        dock1.setWindowTitle("Componente base 1")
        # Asignamos el componente que contendrà
        self.lineEdit = QTextEdit(self)
        dock1.setWidget(self.lineEdit)
        # Le asignamos una anchura mínima de 50
        dock1.setMinimumWidth(300)
        # Lo posicionamos a la derecha de la ventana principal
        self.addDockWidget(Qt.TopDockWidgetArea, dock1)

      
    def abrir_archivo(self):
        f = open("C:/Users/JorgeDAM2/Desktop/Proyecto1/texto.txt", "r")
        self.lineEdit.setText(str(f.read())) 
   

    def guardar_archivo(self):
        f = open("C:/Users/JorgeDAM2/Desktop/Proyecto1/texto.txt", "w")
        f.write(self.lineEdit.toPlainText())
        
        
    def salir(self):
        app.exit()


if __name__ == "__main__":
    app = QApplication([])

    ventana1 = VentanaPrincipal()
    ventana1.show()

    app.exec()