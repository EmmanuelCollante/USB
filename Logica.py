
import tkinter as tk
from tkinter import filedialog
import shutil
import os

root = tk.Tk()
root.withdraw()

class UsbReader():
    def __init__(self):
        pass
    def borrar(self,origen,destino):
        for archivo in os.listdir(destino):
            ruta_origen = os.path.join(origen, archivo)
            ruta_destino = os.path.join(destino, archivo)
            if os.path.isfile(ruta_destino) and not os.path.exists(ruta_origen):
                os.remove(ruta_destino)
                print(f'Archivo eliminado de destino: {archivo}')

    def copiar(self,origen,destino):
        for archivo in os.listdir(origen):
            ruta_origen = os.path.join(origen, archivo)
            ruta_destino = os.path.join(destino, archivo)
            if os.path.isfile(ruta_origen) and not os.path.exists(ruta_destino):
                shutil.copy(ruta_origen, ruta_destino)
                print(f'Archivo copiado a destino: {archivo}')

    def consultar(self):
        nombreCarpeta = filedialog.askdirectory(title='Selecciona la carpeta de la USB')
        if nombreCarpeta:
            print('existe')
            print('Ahora seleccione la carpeta donde va a copiar')
            comparador = filedialog.askdirectory(title='Selecciona la carpeta donde va a copiar')
            if comparador:
                print('existe')
                self.borrar(nombreCarpeta, comparador)
                self.copiar(nombreCarpeta, comparador)
            else:
                print('no existe')       
        else:
            print('no existe')




Usb = UsbReader()
Usb.consultar()