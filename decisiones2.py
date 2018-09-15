comodin = "algo"

#retorna el mensaje correspndiente dependiendo de
#el rango en el que se encuentre la temperatira
#agua

def estado_agua(temperatura):
    if (type(temperatura))== int or type(temperatura)== float:
        if temperatura <=0:
            print ("estado del agua solido")

    elif (temperatura > 0) and (temperatura <= 100):
            print ("estado del agua liquita")

    elif temperatura > 100:
            print ("estado del agua: gaseoso")

    else:
            print ("estado indeterminado: temperatura extraterrestre")
