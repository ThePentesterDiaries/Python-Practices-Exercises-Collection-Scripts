def escritura(datoa,datob,datoc):
    prueba=open('c:Users/sams/datos.py','w')
    prueba.write(datoa)
    prueba.write(datob)
    prueba.write(datoc)
    print "escritura"
    prueba.close


    
escritura('hola', 'Mundo', 'bonito')




def lectura():
    prueba = open('c:Users/sams/datos.py','r')
    print(prueba.read())
    prueba.close()


    
lectura()

