
import tkinter as tk
from tkinter import filedialog
import shutil
import os

root = tk.Tk()
root.withdraw()

class UsbReader():
    def __init__(self):
        pass
    
    def copiar(self,origen,destino):
        for archivo in os.listdir(origen):
            rutaOrigen = os.path.join(origen, archivo)
            rutaDestino = os.path.join(destino, archivo)
            if os.path.isfile(rutaOrigen):
                shutil.copy(rutaOrigen, rutaDestino)
                print('listo')

    def consultar(self):
        nombreCarpeta = filedialog.askdirectory(title='Selecciona la carpeta de la USB')
        if nombreCarpeta:
            print('existe')
            nombre = os.path.basename(nombreCarpeta)
            print(nombre)
            print('Ahora seleccione la carpeta donde va a copiar')
            comparador = filedialog.askdirectory(title='Selecciona la carpeta donde va a copiar')
            nombre2 = os.path.basename(comparador)
            print(nombre2)
            if comparador:
               rutaDestino = os.path.join(comparador, nombre)
               print(rutaDestino)
               if os.path.exists(rutaDestino):
                   print(f"La carpeta '{nombre}' ya existe en la ubicación de destino.")
                   self.copiar(nombreCarpeta, comparador)
               else:
                   os.makedirs(rutaDestino)
                   print(f"Se creó la carpeta '{nombre}' en la ubicación de destino.")

            else:
                print('no existe')       
        else:
            print('no existe')


Usb = UsbReader()
Usb.consultar()