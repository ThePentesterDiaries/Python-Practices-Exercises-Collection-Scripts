class Persona:

     def __init__(self, edad, nombre):
          self.edad = edad
          self.nombre = nombre
          print "Se ha creado a ", self.nombre, " de ", self.edad

     def hablar(self,palabras ):
          print self.nombre, ': ', palabras


juan = Persona()
juan.hablar("Hola amigo")
