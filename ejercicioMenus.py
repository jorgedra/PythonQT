import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Ejercicio Menus")

        layout_principal = QHBoxLayout()

        self.stack = QStackedLayout()
        self.uno = QHBoxLayout()
        self.dos = QHBoxLayout()


        barraMenu1 =  self.menuBar()
        menu1 = barraMenu1.addMenu("&Archivo")
        menu2 = barraMenu1.addMenu("&Editar")
        menu3 = barraMenu1.addMenu("&Ver")
        prevMenu = QMenu('Tipo de documento',self)
        doc1 = QAction("&PDF",prevMenu)
        doc2 = QAction("&Carta",prevMenu)
        doc3 = QAction("&Email",prevMenu)
        menu3.addMenu(prevMenu)
        prevMenu.addAction(doc1)
        prevMenu.addAction(doc2)
        prevMenu.addAction(doc3)

        barra_Herramientas = QToolBar("Barra 1")
        
        ruta_icono1 = os.path.join(os.path.dirname(__file__), "imgs/letra.png")
        ruta_icono2 = os.path.join(os.path.dirname(__file__), "imgs/letraVerde.png")

        accion1 = QAction("&Copiar archivo" ,self)
        accion1.setShortcut(QKeySequence("Ctrl+c"))
        accion1.triggered.connect(self.copiarArchivo)

        accion2 = QAction("&Pegar archivo" ,self)
        accion2.setShortcut(QKeySequence("Ctrl+v"))
        accion2.triggered.connect(self.pegarArchivo)

        accion3 = QAction("&Eliminar archivo" ,self)
        accion3.setShortcut(QKeySequence("Ctrl+x"))
        accion3.triggered.connect(self.eliminarArchivo)

        accion4 = QAction("&Cambiar texto a mayusculas" ,self)
        accion4.setShortcut(QKeySequence("Ctrl+u"))
        accion4.triggered.connect(self.cambiarMayus)

        accion5 = QAction("&Cambiar texto a minisculas" ,self)
        accion5.setShortcut(QKeySequence("Ctrl+l"))
        accion5.triggered.connect(self.cambiarMinus)

        accion6 = QAction(QIcon(ruta_icono2),"&Cambiar color texto" ,self)
        accion6.setWhatsThis("cambiar el color de la consola a verde")
        accion6.setShortcut(QKeySequence("Ctrl+t"))
        accion6.triggered.connect(self.cambiarColor)

        accion7 = QAction(QIcon(ruta_icono1),"&Volver al color normal" ,self)
        accion7.setWhatsThis("cambiar el color de la consola al color por defecto")
        accion7.setShortcut(QKeySequence("Ctrl+n"))
        accion7.triggered.connect(self.cambiarColorN)

        accion8 = QAction("&Modo diseño" ,self)
        accion8.setShortcut(QKeySequence("Ctrl+d"))

        accion9 = QAction("&Modo lectura" ,self)
        accion9.setShortcut(QKeySequence("Ctrl+r"))

        self.label1 = QLabel("Ventana uno")
        self.label2 = QLabel("Ventana dos")
        self.boton = QPushButton("Ir a dos")
        self.boton.clicked.connect(self.cambiar)
        self.uno.addWidget(self.label1)
        self.uno.addWidget(self.boton)

        self.dos.addWidget(self.label2)

        
        menu1.addAction(accion1)
        menu1.addAction(accion2)
        menu1.addAction(accion3)

        menu2.addAction(accion4)
        menu2.addAction(accion5)
        menu2.addAction(accion6)
        menu2.addAction(accion7)

        menu3.addAction(accion8)
        menu3.addAction(accion9)

        barra_Herramientas.addAction(accion6)
        barra_Herramientas.addAction(accion7)

        self.addToolBar(barra_Herramientas)


        layour_login = QWidget()
        layour_login.setLayout(self.uno)

        layour_error = QWidget()
        layour_error.setLayout(self.dos)

        self.stack.addWidget(layour_login)
        self.stack.addWidget(layour_error)

        componente_principal = QWidget()

        componente_principal.setLayout(layout_principal)
        self.setCentralWidget(componente_principal)

        layout_principal.addLayout(self.stack)


    def copiarArchivo(self):
        print("Archivo copiado con exito")
    def pegarArchivo(self):
        print("Archivo pegado con exito")
    def eliminarArchivo(self):
        print("Archivo eliminado con exito")
    def cambiarMayus(self):
        print("AHORA EL ARCHIVO ENTERO ESTA GRITANDO")
    def cambiarMinus(self):
        print("Parece que el archivo se ha relajado un poco y no grita tanto")
    def cambiarColor(self):
        print(bcolors.OKGREEN + "Color del texto cambiado a verde")
    def cambiarColorN(self):
        print(bcolors.ENDC + "Color cambiado al color por defecto")
    def cambiar(self):
        self.stack.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show()
    app.exec()
