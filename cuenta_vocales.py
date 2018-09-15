#creacion de un cuenta vocales
def cuenta_vocales(s):
    '''
(str) -> int
>>>contador_vocales("un string")
9
>>>contador_vocales("MVP")
0
   '''
    num_vocales = 0
    for caracter in s:
        if caracter in 'aeiouAEIOU':
            num_vocales = num_vocales + 1
    return num_vocales


def acumula_vocales(s):
    '''(str)-> str
Devuelve las vocales que tiene s.
>>>acumula_vocales("videotutoriales.com")
'ieouiaeo'
'''
    vocales = ''
    for caracter in s:
        if caracter in "aeiouAEIOU":
            vocales = vocales + caracter
    return vocales


