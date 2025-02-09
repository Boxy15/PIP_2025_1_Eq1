import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P07_PromedioNumeros-Load.ui" # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.btn_Agregar.clicked.connect(self.agregar)
        self.btn_Guardar.clicked.connect(self.guardar)
        self.btn_Cargar.clicked.connect(self.cargar)
        self.calificaciones = []

    # Area de los slots
    def cargar(self):
        # archivo=open
        # TAREA como compruebo si el archivo existe #ejercicio 10
        if self.cargas >= 1:
            self.msj("No puedes cargar otro archivo")
            return
        archivo = open("../Archivos/calificaciones.csv")
        contenido = archivo.readlines()
        print(contenido)
        datos = [int(x) for x in contenido]
        print(datos)
        self.calificaciones = datos
        self.cargas += 1

    def agregar(self):
        calificacion = int(self.txt_Calif.text())
        self.calificaciones.append(calificacion)
        prom = sum(self.calificaciones) / len(self.calificaciones)
        self.txt_Promedio.setText(str(prom))

    def guardar(self):
        archivo = open('calificaciones.csv', 'a')
        for i in self.calificaciones:
            archivo.write(str(i)+'\n')
        archivo.flush()
        archivo.close()
        self.msj("Archivo Guardado con éxito")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())