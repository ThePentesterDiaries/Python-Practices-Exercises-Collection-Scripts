#calculo de areas

F = 3.141516

#area del cuadrado

def cuadrado():
    lado = input ("cual es el valor del lado ")
    x = (lado ** 2)
    print ("el area del cuadrado es ",x)


def triangulo():
    base = input("cual es el valor de la base")
    altura = input("cual es el valor de la altura")
    y = (base * altura / 2)
    print ("el area del triangulo es ",y)


def circulo():
    radio = input("cual es valor del radio")
    z = (F * radio) ** 2
    print ("el area del circulo es",z)


i = True 

while i==True:
    area = input("elige una figura geometrica para calcular su area \nCuadrado = 1 \nTriangulo = 2 \nCirculo = 3\n")

    if area==1:
        cuadrado()

    elif area==2:
        triangulo()

    elif area==3:
        circulo()

    else:
        print ("ingresa una opcion valida")

i = input("\nQuieres calcular el area de otra figura? \nSi=True \nNo=False\n")
