from tkinter import *
from tkinter import ttk,font, messagebox
import tkinter as tk
import requests
class Aplicacion():
    __ventana = None
    __dolares = None
    __pesos = None
    
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Conversor de moneda')
        fuente=font.Font(font='Verdana 10',weight='normal')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        
        self.__dolares = StringVar()
        self.__pesos = StringVar()
        
        self.__dolares.trace('w',self.calcular)
        self.dolaresEntry = ttk.Entry(mainframe, width=15, textvariable=self.__dolares)
        self.dolaresEntry.grid(column=1,row=0,padx=10,pady=10)
        ttk.Label(mainframe, text="dólares").grid(column=2, row=0,padx=10,pady=10)
        
        
        ttk.Label(mainframe, text="es equivalente a ").grid(column=0, row=1,padx=10,pady=10)
        ttk.Label(mainframe, textvariable=self.__pesos).grid(column=1, row=1,padx=10,pady=10)
        ttk.Label(mainframe, text="pesos").grid(column=2, row=1,padx=10,pady=10)
        
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=2, row=2, sticky=W)
        self.__ventana.mainloop()

    def calcular(self, *args):
        

        URL ='https://www.dolarsi.com/api/api.php?type=dolar'

        json = requests.get(URL).json()
        for index in range (1):
            venta = json[index]['casa']['venta'][:-1]
        venta = venta.replace(',','.')
        if self.dolaresEntry.get()!='':
            try:
                dolares = float(self.__dolares.get())
                self.__pesos.set(dolares*float(venta))
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar valores numéricos')
                self.__dolares.set('')
        else:
            self.__pesos.set('')

def testApp():
    mi_app=Aplicacion()

if __name__ == '__main__':
    testApp()