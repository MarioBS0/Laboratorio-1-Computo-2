import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class Mascotas(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Datos de 3 Mascotas")
        self.setGeometry(100, 100, 400, 200)

        # Crear etiquetas para mostrar los datos de las tres mascotas
        self.mascotas = QLabel("Mascota 1 - Nombre: Canlea, Animal: Perro, Edad: 5 años \nMascota 2 - Nombre: Azul, Animal: Gato, Edad: 3 años \nMascota 3 - Nombre: Draxi, Animal: Perro, Edad: 1 año")

        self.mascotas.setStyleSheet("font: 12pt Century Gothic;")

        # Crear un layout vertical y añadir las etiquetas
        layout = QVBoxLayout()
        self.mascotas.setAlignment(Qt.AlignCenter) 
        # Añadir datos de la primera mascota
        layout.addWidget(self.mascotas) 
        # Ajustar los márgenes (izquierda, arriba, derecha, abajo)
        layout.setContentsMargins(10, 10, 10, 10) 
        # Establecer el layout en la ventana
        self.setLayout(layout)

if __name__ == "__main__":
     # Crear instancia de la aplicacion
    app = QApplication(sys.argv)  
     #Para la ventana      
    window = Mascotas()
    #Esto es para mostrar la ventana            
    window.show()                        
    sys.exit(app.exec_())               

#Esto es el ultimo ejercicio 👻👻👻