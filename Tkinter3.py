from Tkinter import *

class interfaz:
    def __init__(self,contenedor):
        self.e1 = Label(contenedor,text="etiqueta1", fg="green", bg="black")
        self.e1.place(x=20,y=30,width=120,height=25)

        
##      self.e1.pack(side=TOP)
        # self.e2.pack(side=RIGHT)

        #self.e3.pack(side=BOTTOM, fill=X)
        

        self.e1.grid(column=0,row=0)
        
        


ventana = Tk()
miinterfaz = interfaz(ventana)
ventana.mainloop()

