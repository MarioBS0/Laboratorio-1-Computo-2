import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
#Nombre de la clase
class InfoVentana(QWidget):
    def __init__(self):
        super().__init__()

        #Configuración de la ventana
        self.setWindowTitle("Información Personal")  # Título de la ventana
        #Tamaño y posición de la ventana
        self.setGeometry(100, 100, 300, 100)        

        #Crear etiquetas para mostrar el número de cédula y el nombre completo
        self.cedula = QLabel("Número de Cédula: 123456789") 
        self.cedula.setStyleSheet("font: 15pt Century Gothic;")  #la fuente y tamaño que quiero que tenga
        
        #Ya en otro codigo puse mi nombre entonces aqui ira su nombre completo inge.

        self.nombre = QLabel("Nombre Completo: William Alexis Montes Giron") 
        self.nombre.setStyleSheet("font: 15pt Century Gothic;")  #la fuente y tamaño que quiero que tenga

        #Crear un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.cedula)  
        layout.addWidget(self.nombre) 

        #Configurar el layout en la ventana
        self.setLayout(layout)

if __name__ == "__main__":
    #Crear una instancia de la aplicación
    app = QApplication(sys.argv)  
    #Crear una instancia de la ventana      
    window = InfoVentana()    
    #Mostrar la ventana          
    window.show()      
    #Ejecutar el bucle de eventos de la aplicación              
    sys.exit(app.exec_())             
