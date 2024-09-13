#importamos lo que necesitaremos
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

#creamos la ventana o es espacio para la ventana
def ventana():
    app = QApplication(sys.argv)
    
    # Esto es para crear la vetana
    ventana = QWidget()
    ventana.setWindowTitle("Nombre y Edad")
    ventana.setGeometry(100,200,300,200)
    
    # Las variables de mi nombre y mi edad
    nombre = "Mario Barahona"
    edad = "20 años"
    
    # Crear la etiqueta
    etiqueta = QLabel(f"Nombre: "+ nombre +"\nEdad: "+ edad +"", ventana)
    etiqueta.setAlignment(Qt.AlignCenter) #Para que se aline en el centro
    etiqueta.setStyleSheet("font: 20pt Century Gothic;")  #la fuente y tamaño que quiero que tenga
    
    # Configurar el layout
    layout = QVBoxLayout()
    layout.addWidget(etiqueta)
    ventana.setLayout(layout)
    
    #Mostrar la ventana
    ventana.show()
    #Ejecutar el bucle principal
    sys.exit(app.exec_())
ventana()#cerramos la def de ventana



#Investigando econtre otra manera de hacerlo con otro import

"""
import tkinter as tk

def ventana():
    ventana = tk.Tk()
    ventana.title("Nombre y Edad")

    nombre = "Nombre"
    edad = "edad"
    
    etiqueta = tk.Label(ventana, text=f"Nombre:"+ nombre +"\nEdad: '+ edad +'", font=("Arial", 20), justify="center")
    etiqueta.pack(expand=True)

    ventana.mainloop()

ventana()

"""
