def escritura(datoa,datob,datoc):
    prueba=open("C:/Users/sams/Desktop/datos.py",'w')
    prueba.write(datoa)
    prueba.write(datob)
    prueba.write(datoc)
    print "escritura"
    prueba.close


    
escritura('hola', 'Mundo', 'bonito')




def lectura():
    prueba = open("C:/Users/sams/Desktop/datos.py",'r')
    print(prueba.read())
    prueba.close()


    
lectura()



##creacion de listas y sus metodos 
lista3 = [23,84,(23,53,98),31]
lista3.remove(31)
print(lista3)

cadena3 = ("somos el milagro de la fuerza y la materia convirtiendose a si mismas en imaginacion y voluntad")
print(cadena3.replace("transformandose","convirtiendose"))
