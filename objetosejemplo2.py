class Animal:
    def nacer(self):
        print ("ha nacido")

    def mover1(self):
        print ("se mueve con extremidades")



class Pez(Animal):
    def respirar(self):
        print ("respira por branquias")

    def mover(self):
        print ("se mueve con aletas")

    



tiburon = Pez()
tiburon.mover1()
