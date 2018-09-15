import sqlite3

def consultar():
    db2 = sqlite3.connect("novelas.db")
    print("estas en la funcion insertar")
    db2.row_factory = sqlite3.Row
    consulta = db2.cursor()
    consulta.execute("select * from tabla")
    filas = consulta.fetchall()

    lista = []

    for fila in filas:
        s = {}

        s['nombre'] = fila['nombre']
        s['autor'] = fila['autor']
        s['year'] = str(fila['year'])

        lista.append(s)

    consulta.close()
    db2.close()
    return(lista)

    

consultar()


def menu():
    Opcion = input("\nIngresa la opcion deseada\n1, insertar un valor\n2, consultar los valores de la tabla \n")
    if Opcion==1:
        insertar()
        menu()

    elif Opcion==2:
        ListaNovelas = consultar()
        for novela in LitaNovelas:
            print(novela['nombre'],novela['autor'],novela['year'])
        menu()

    menu()
