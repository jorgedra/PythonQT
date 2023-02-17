import os
import platform

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class DialogoPersonalizado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("¿Estas seguro de cerrar el archivo?")

        # Definimos los botones Ok i Cancel en nuestra variable
        botones = QDialogButtonBox.Close| QDialogButtonBox.Open

        # Pasamos la variable de botones al constructor de QDialogButtonBox
        self.caja_botones = QDialogButtonBox(botones)
        # Conectamos las señales de los botones con las ranuras de QDialog
        self.caja_botones.accepted.connect(self.accept)
        self.caja_botones.rejected.connect(self.reject)
        

        # Añadimos un QLabel y el QDialogButtonBox en un layout vertical
        self.layout_dialogo = QVBoxLayout()
        self.layout_dialogo.addWidget(QLabel("Open para abrir uno nuevo y close para guardar y cerrar el programa"))
        self.layout_dialogo.addWidget(self.caja_botones)
        self.setLayout(self.layout_dialogo)
    
  

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

        self.accion4 = QAction("Cerrar y abrir otro", self)
        self.accion4.setStatusTip("Cerrar y abrir otro")
        self.accion4.setShortcut(QKeySequence("Ctrl+l"))
        self.accion4.triggered.connect(self.abrir_otro_archivo)

        menu.addAction(self.accion)
        menu.addAction(self.accion2)
        menu.addAction(self.accion3)
        menu.addAction(self.accion4)

        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(self.accion)
        barra_herramientas.addAction(self.accion2)
        barra_herramientas.addAction(self.accion3)
        barra_herramientas.addAction(self.accion4)

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
        self.archivo = None

      
    def abrir_otro_archivo(self):
        ventana_dialogo = DialogoPersonalizado(self)
        resultado = ventana_dialogo.exec()
        if resultado:
            self.archivo = None
            ventana_dialogo = QFileDialog.getOpenFileName(
            self, caption="Abrir archivo ...", dir=".",
            filter="Documentos de texto (*.txt);;Documentos PDF (*.pdf)",
            selectedFilter="Documentos de texto (*.txt)")
            self.archivo = ventana_dialogo[0]
            f = open(self.archivo, "r")
            self.lineEdit.setText(str(f.read())) 
            print(self.archivo)
        else:
            if self.archivo == None:
                ventana_dialogo = QFileDialog.getSaveFileName(
                    self, caption="Guardar archivo ...", dir=".",
                    filter="Documentos de texto (*.txt);;Documentos PDF (*.pdf)",
                    selectedFilter="Documentos de texto (*.txt)")
                self.archivo = ventana_dialogo[0]
                print(self.archivo)
                f = open(self.archivo, "w")
                f.write(self.lineEdit.toPlainText())
                app.exit()
            else:
                f = open(self.archivo,"w")
                f.write(self.lineEdit.toPlainText())
                app.exit()
   

    def guardar_archivo(self):
        if self.archivo == None:
            ventana_dialogo = QFileDialog.getSaveFileName(
                self, caption="Guardar archivo ...", dir=".",
                filter="Documentos de texto (*.txt);;Documentos PDF (*.pdf)",
                selectedFilter="Documentos de texto (*.txt)")
            self.archivo = ventana_dialogo[0]
            print(self.archivo)
            f = open(self.archivo, "w")
            f.write(self.lineEdit.toPlainText())
        else:
            f = open(self.archivo,"w")
            f.write(self.lineEdit.toPlainText())
        
        
    def salir(self):
        app.exit()

    def abrir_archivo(self):
        ventana_dialogo = QFileDialog.getOpenFileName(
            self, caption="Abrir archivo ...", dir=".",
            filter="Documentos de texto (*.txt);;Documentos PDF (*.pdf)",
            selectedFilter="Documentos de texto (*.txt)")
        self.archivo = ventana_dialogo[0]
        f = open(self.archivo, "r")
        self.lineEdit.setText(str(f.read())) 
        print(self.archivo)

    def cargar_traductor(app):
        translator = QTranslator(app)
        translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        translator.load("qt_es", translations)
        app.installTranslator(translator)

    
if __name__ == "__main__":
    app = QApplication([])
    
    ventana1 = VentanaPrincipal()
    ventana1.show()

    app.exec()