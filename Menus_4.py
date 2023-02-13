import os
import platform

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "Ventana principal con menú, barra de herramientas " +
            " y barra de estado")

        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        self.edit = QTextEdit()
        ruta_a_icono = os.path.join(os.path.dirname(
            __file__), "consola.png")
        ruta_a_icono2 = os.path.join(os.path.dirname(
            __file__), "question.png")
        self.accion = QAction(QIcon(ruta_a_icono), "Imprimir en dock", self)
        self.accion2 = QAction(QIcon(ruta_a_icono2), "Activar ayuda", self)
        self.accion.setWhatsThis(
            "Al ejecutar esta acción, se añadirá el texto 'Acción pulsada' en el dock."
            + "Se puede lanzar por Menú > Imprimir en dock, con Ctrl + P o haciendo clic" 
            + "en el botón correspondiente de la barra de herramientas")
        self.accion.setStatusTip("Imprimir por consola")
        self.accion.setShortcut(QKeySequence("Ctrl+p"))
        self.accion.triggered.connect(self.imprimir_por_consola)
        menu.addAction(self.accion)

        self.accion2.setStatusTip("Activar ayuda")
        self.accion2.setShortcut(QKeySequence("Shift+F1"))
        self.accion2.triggered.connect(self.activar_ayuda)

        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(self.accion)
        barra_herramientas.addAction(self.accion2)
        self.addToolBar(barra_herramientas)

        barra_estado = self.statusBar()
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        barra_estado.showMessage("Listo. Esperando acción ...", 3000)

        # Creamos un componente flotante
        dock1 = QDockWidget()
        # Agregamos título a este componente
        dock1.setWindowTitle("Componente base 1")
        # Asignamos el componente que contendrà
        dock1.setWidget(self.edit)
        # Le asignamos una anchura mínima de 50
        dock1.setMinimumWidth(100)
        # Lo posicionamos a la derecha de la ventana principal
        self.addDockWidget(Qt.TopDockWidgetArea, dock1)

        self.setCentralWidget(QLabel("Componente principal"))

    def imprimir_por_consola(self):
        textoEdit = self.edit.toPlainText()
        self.edit.setText(textoEdit + " Accion pulsada")

    def activar_ayuda(self):
        ws = QWhatsThis("Modo ayuda",self)    
        ws.enterWhatsThisMode()    


if __name__ == "__main__":
    app = QApplication([])

    ventana1 = VentanaPrincipal()
    ventana1.show()

    app.exec()
