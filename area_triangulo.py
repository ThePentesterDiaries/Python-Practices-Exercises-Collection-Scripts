import math 

def area_triangulo(base,altura):
    '''(number,number)->number
devuelve el area de un triangulo al pasarle base y altura'''
    area = base * altura / 2
    return area

def perimetro_triangulo(a,b,c):
    '''(numero,numero,numero)->
devuelve el perimetro de un triangulo al pasarle los 3 argumentos'''
    perimetro = (a+b+c)
    return perimetro

def diagonal_rectangulo(ancho,alto):
    '''(number,number)->float
    >>>diagonal_rectangulo(10,6)
    11.66 '''
    suma_cuadrados = (ancho ** 2) + (alto**2)
    diagonal = math.sqrt(suma_cuadrados)
    return diagonal


