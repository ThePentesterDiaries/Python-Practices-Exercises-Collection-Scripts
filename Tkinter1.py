from Tkinter import *

class interfaz:
    def __init__(self,contenedor):
        self.e1 = Label(contenedor,text="etiqueta1", fg="green", bg="black")
        self.e2 = Label(contenedor, text="etiqueta2",fg="black", bg="gray")
        self.e3 = Label(contenedor, text="etiqueta3",fg="black", bg="green")
        
        self.e1.pack(side=TOP)
        self.e2.pack(side=RIGHT)
        self.e3.pack(side=BOTTOM, fill=X)
        
        
        



ventana = Tk()
miinterfaz = interfaz(ventana)
ventana.mainloop()


