import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P06_PromedioNumeros.ui" # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.btn_Agregar.clicked.connect(self.agregar)
        self.btn_Guardar.clicked.connect(self.guardar)
        self.calificaciones = []

    # Area de los slots
    def agregar(self):
        calificacion = int(self.txt_Calif.text())
        self.calificaciones.append(calificacion)
        prom = sum(self.calificaciones) / len(self.calificaciones)
        self.txt_Promedio.setText(str(prom))

    def guardar(self):
        archivo = open('calificaciones.csv', 'w')
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