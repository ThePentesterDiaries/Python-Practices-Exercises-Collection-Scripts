from Tkinter import *

class interfaz:
    def __init__(self,contenedor):
        self.e1 = Label(contenedor,text="etiqueta1", fg="green", bg="black")
        self.e2 = Label(contenedor, text="etiqueta2",fg="black", bg="gray")
        self.e3 = Label(contenedor, text="etiqueta3",fg="black", bg="green")
        self.e4 = Label(contenedor, text="etiqueta4",fg="black", bg="blue")
        self.e5 = Label(contenedor, text="etiqueta5",fg="black", bg="red")
        self.e6 = Label(contenedor, text="etiqueta6",fg="black", bg="pink")


        
##      self.e1.pack(side=TOP)
        # self.e2.pack(side=RIGHT)

        #self.e3.pack(side=BOTTOM, fill=X)
        

        self.e1.grid(column=0,row=0)
        self.e2.grid(column=0,row=1)
        self.e3.grid(column=0,row=2)
        self.e4.grid(column=1,row=0)
        self.e5.grid(column=1,row=1)
        self.e6.grid(column=1,row=2)
        
        


ventana = Tk()
miinterfaz = interfaz(ventana)
ventana.mainloop()


