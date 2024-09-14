import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class Datos(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Datos Caracteristicos de una Persona")
        self.setGeometry(100, 100, 400, 300)

        # Crear etiquetas para mostrar los 10 datos característicos de una persona
        self.nombre = QLabel("1-Nombre: Mario Barahona")
        self.edad = QLabel("2-Edad: 20 años")
        self.altura = QLabel("3-Altura: 1.80 metros")
        self.peso = QLabel("4-Peso: 182 lbs")
        self.ocupacion = QLabel("5-Ocupación: Estudiante en Ingeniero de sistemas")
        self.nacionalidad = QLabel("6-Nacionalidad: Salvadorena")
        self.direccion = QLabel("7-Dirección: Calle Falsa 123, San Miguel")
        self.telefono = QLabel("8-Teléfono: +503 7223-1112")
        self.email = QLabel("9-Email: mario123@email.com")
        self.estadoCivil = QLabel("10-Estado Civil: Soltero")

        # Crear un layout vertical y añadir las etiquetas
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)  # Ajustar márgenes para que esté organizado
        layout.setSpacing(10)  # Espaciado entre los datos

        # Añadir todas las etiquetas al layout
        layout.addWidget(self.nombre)
        layout.addWidget(self.edad)
        layout.addWidget(self.altura)
        layout.addWidget(self.peso)
        layout.addWidget(self.ocupacion)
        layout.addWidget(self.nacionalidad)
        layout.addWidget(self.direccion)
        layout.addWidget(self.telefono)
        layout.addWidget(self.email)
        layout.addWidget(self.estadoCivil)

        # Establecer el layout en la ventana
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)         
    window = Datos()             
    window.show()                        
    sys.exit(app.exec_())  

#Esto es el ultimo ejercicio 👻👻👻
