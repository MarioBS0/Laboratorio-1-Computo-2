#Importamos las herramientas
import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QPushButton, QWidget

#la clase para nuestra clave secreta 🤫
class ClaveSecreta(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Ingreso de Clave Secreta")
        self.setGeometry(100, 100, 300, 100)

        # Crear y configurar el campo de entrada para la clave secreta
        self.contra = QLineEdit()
        self.contra.setEchoMode(QLineEdit.Password)  # Ocultar los caracteres ingresados

        # Crear y configurar el botón
        self.boton = QPushButton("Mostrar Clave (en la terminal)")
        # Conectar el botón a la función que muestra la clave
        self.boton.clicked.connect(self.mostrar)  

        # Crear y configurar el layout
        layout = QVBoxLayout()
        # Añadir el campo de entrada al layout
        layout.addWidget(self.contra)  
        #Añadir el botón al layout
        layout.addWidget(self.boton)
        #Configurar el layout en la ventana    
        self.setLayout(layout)                 

    def mostrar(self):
        # Mostrar la clave en la consola al presionar el botón
        print(f"La clave secreta ingresada es: "+ self.contra.text())

if __name__ == "__main__":
    # Crear una instancia de la aplicación
    app = QApplication(sys.argv) 
    #Crear una instancia de la ventana
    window = ClaveSecreta()
     # Mostrar la ventana      
    window.show()  
    # Ejecutar el bucle de eventos de la aplicación                 
    sys.exit(app.exec_())  
          
