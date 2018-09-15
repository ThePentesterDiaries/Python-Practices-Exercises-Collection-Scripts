from abc import ABCMeta, abstractmethod

class Persona:
    __metaclass__=ABCMeta
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("se ha creado a", self.nombre,"de",self.edad)

    @abstractmethod
    def hablar(self,**palabras): pass
##         for frase in palabras:
##              print(self.nombre, ':', frase)

     

class Deportista(Persona):
    def __init__(self,edad,nombre,deporte):
        self.edad = edad
        self.nombre = nombre
###     self.deporte = deporte
####    la de abajo es una instancia de un atributo privado con __
        self.__deporte = deporte
        print("se ha creado a", self.nombre,"de",self.edad

    def practicarDeporte(self):
        print(self.nombre, ":voy a practicar natacion")

   def verMiDeporte(self):
##            aqui abajo se retorna el valor privado del atributo deporte 
        return self.__deporte
   
   def hablar(self,*palabras):
              for frase in palabras:
                  print (self.nombre, ":", luis.verMiDeporte())

   
   
##objetos y modificaciones e interacciones de estos 
##juan = Persona(18, "juan")
##juan.hablar(t1="hola estoy hablando", t2="este soy yo")
luis = Persona(20, "luis")
luis = Deportista(18,"luis")
luis.hablar(t1="hola estoy hablando y soy luis",t2="este soy yo")
luis.practicarDeporte()
print ("luis practica", luis.__deporte())
print ("luis practica", luis.verMiDeporte())



