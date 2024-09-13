import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QRadioButton, QComboBox, QSpinBox, QPushButton, QMessageBox

class Formulario(QWidget):
    def __init__(self):
        super().__init__()

        # Configuracion de la ventana
        self.setWindowTitle("Formulario de Informacion")
        self.setGeometry(100, 200, 300, 200)

        # Crear layout vertical
        layout = QVBoxLayout()

        # Etiqueta de genero
        self.genero = QLabel("Seleccione su genero:")
        layout.addWidget(self.genero)

        # Radios para seleccionar el género
        self.RadioMasculino = QRadioButton("Masculino")
        self.RadioFemenino = QRadioButton("Femenino")
        layout.addWidget(self.RadioMasculino)
        layout.addWidget(self.RadioFemenino)

        #Etiqueta de pais de residencia
        self.pais = QLabel("Seleccione su pais de residencia:")
        layout.addWidget(self.pais)

        #Combobox para seleccionar el pais
        self.opcionesPaises = QComboBox()
        #Opicnes de eleccion para el pais
        self.opcionesPaises.addItems(["El Salvador", "Honduras", "Guatemala", "Panama", "Estados Unidos"])
        layout.addWidget(self.opcionesPaises)


        # Boton para mostrar los datos ingresados
        self.boton= QPushButton("Enviar")
        self.boton.clicked.connect(self.show_data)
        layout.addWidget(self.boton)

        # Establecer el layout en la ventana
        self.setLayout(layout)

    def show_data(self):
        # Obtener el genero seleccionado
        if self.RadioMasculino.isChecked():
            sexo = "Masculino"
        elif self.RadioFemenino.isChecked():
            sexo = "Femenino"
        else:
            sexo = "No seleccionado"

        # Obtener el país seleccionado
        Pais1 = self.opcionesPaises.currentText()

        # Mostrar los datos en un mensaje emergente
        mensaje = f"Género: "+ sexo + "\nPaís: "+ Pais1 +""
        QMessageBox.information(self, "Datos Ingresados", mensaje)

if __name__ == "__main__":
    app = QApplication(sys.argv)         
    window = Formulario()               
    window.show()                   
    sys.exit(app.exec_())              
