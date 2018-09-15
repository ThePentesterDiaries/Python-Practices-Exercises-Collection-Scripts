def faltan_pruebas():
    pruebas_totales = 12
    pruebas_pasadas = input("cuantas pruebas has pasado")
    diferencia = pruebas_totales - int(pruebas_pasadas)
    diferencia = str(diferencia)
    return "te faltan por pasar un total de" + diferencia + "pruebas"


