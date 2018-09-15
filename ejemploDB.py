import sqlite3

def insertar():
    db1=sqlite3.connect('novelas.db')
    print("estas en la funcion insertar")

    nombre1=raw_input("escribe el titulo de la novela")
    autor1=raw_input("escribe el autor de la novela")
    year1=str(input("digita el anio e la novela"))

    consulta=db1.cursor()

    strConsulta = "insert into tabla(nombre,autor,year)  values (""+nombre1+"",""+autor1+"",""+year+"")"
    print(strConsulta)

    consulta.close()
    db1.commit()
    db1.close()






insertar()
