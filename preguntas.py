"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def leer_data_csv():
    with open("data.csv", "r") as file:
        data = list(csv.reader(file, delimiter="\t"))
        # for row in data:
        #     print(row)
    return data

#data=leer_data_csv()
#print(data)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = leer_data_csv()
    suma = 0

    for row in data:
        suma += int(row[1])
    return suma

#Resultado1= pregunta_01()  
#print(f"La suma es: {Resultado}")
   


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = leer_data_csv()
    letra_cantidad = {} #crear un diccionario vacioo 

    for i in data:
        letra = i[0]
        if letra in letra_cantidad:
            letra_cantidad[letra] += 1
        else:
            letra_cantidad[letra] = 1

    # Convierte el diccionario a una lista de tuplas y ordénala alfabéticamente por la letra
    resultado = sorted(letra_cantidad.items(), key=lambda x: x[0])


    return resultado

#Resultado2= pregunta_02()  
#print(Resultado)



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = leer_data_csv()
    words_p3 = {}

    for i in data:
        if i[0] in words_p3.keys():
            words_p3[i[0]] += int(i[1])
        else:
            words_p3[i[0]] = int(i[1])
    sorted_words_p3 = sorted(words_p3.items())
    return sorted_words_p3

#Resultado3= pregunta_03()  
#print(Resultado)



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = leer_data_csv()
    Months_r = {}

    # Iterar sobre cada fila de los datos
    for i in data:
        # Utilizar el método split para extraer el mes de la columna 3 (formato YYYY-MM-DD)
        Months = i[2].split('-')[1]

        
        if Months in Months_r:
            
            Months_r[Months] += 1
        else:
            
            Months_r[Months] = 1

   
    resultado = sorted(Months_r.items())

    return resultado


#Resultado4 = pregunta_04()
#print(Resultado)
    
    


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = leer_data_csv ()
    word_value = {}

    for i in data:
        word = i[0]  # Obtener la letra de la columna 1
        value = int(i[1])  # Obtener el valor de la columna 2
            # Si la letra ya está en el diccionario, se agrega el valor a la lista existente
        if word in word_value:
            word_value [word].append(value)
        else:
            word_value[word] = [value]

    # Lista vacia para almacenar las tuplas de resultado
    resultado = []

# Iterar sobre el diccionario y encontrar el valor máximo y mínimo por cada letra
    for words, values in word_value.items():
            valor_max = max(values)
            valor_min = min(values)
            resultado.append((words, valor_max, valor_min))
            resultado_ordenado_p5 = sorted(list(resultado))
    return (resultado_ordenado_p5)

#Resultado5 = pregunta_05()
#print(Resultado)

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = leer_data_csv ()
    word_value = {}

    # Iterar sobre cada fila del archivo CSV
    for i in data:
        diccionario_codificado = i[4]
        diccionario = {}
        for z in diccionario_codificado.split(","):
            clave, valor = z.split(":")
            diccionario[clave] = int(valor)
        
        # Actualizar los valores mínimo y máximo para cada clave
        for clave, valor in diccionario.items():
            if clave in word_value:
                word_value[clave] = (min(word_value[clave][0], valor), max(word_value[clave][1], valor))
            else:
                word_value[clave] = (valor, valor)
    
    # Convertir el diccionario a una lista de tuplas
    resultado_tuplas = [(clave, valores[0], valores[1]) for clave, valores in word_value.items()]

    # Ordenar la lista de tuplas por clave
    resultado_ordenado_p6 = sorted(list(resultado_tuplas))
    return resultado_ordenado_p6

#Resultado = pregunta_06()
#print(Resultado)

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    
    data = leer_data_csv()
    words_value = {}

    # Iterar sobre cada fila de los datos
    for i in data:
        valor_columna_dos = int(i[1])
        letra = i[0]

       
        if valor_columna_dos in words_value:
        
            words_value[valor_columna_dos].append(letra)
        else:
            
            words_value[valor_columna_dos] = [letra]

    # Convertir el diccionario a una lista de tuplas y ordenarla por el valor de la columna 2
    resultado = sorted(words_value.items())

    return resultado


#Resultado = pregunta_07()
#print(Resultado)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    
    data = leer_data_csv()
    words_value = {}

    
    for row in data:
        valor_columna_dos = int(row[1])
        letra = row[0]

        
        if valor_columna_dos in words_value:
            
            words_value[valor_columna_dos].append(letra)
        else:
            
            words_value[valor_columna_dos] = [letra]

    # Convertir el diccionario a una lista de tuplas con las letras ordenadas y sin repetir letra
    resultado = sorted([(valor, sorted(set(letras))) for valor, letras in words_value.items()], key=lambda x: x[0])

    return resultado


#Resultado = pregunta_08()
#print(Resultado)

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = leer_data_csv()
    word_value = {}

    for row in data:
        for i in row[4].split(","):
            clave = i.split(":")[0]
        
            if clave in word_value.keys():
                word_value[clave] +=1
            else:
                word_value[clave] = 1

    registros_ordenados = dict(sorted(word_value.items()))
    return registros_ordenados



#Resultado = pregunta_09()
#print(Resultado)



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = leer_data_csv()
    lista_tuplas = []

    # Iterar sobre cada fila del archivo CSV
    for i in data:
        letra_columna1 = i[0]   # Obtener la letra de la columna 1
        elementos_columna4 = len(i[3].split(","))  # Contar los elementos de la columna 4
        elementos_columna5 = len(i[4].split(","))  # Contar los elementos de la columna 5

        # Crear una tupla con la letra de la columna 1 y la cantidad de elementos de las columnas 4 y 5
        tupla = (letra_columna1, elementos_columna4 , elementos_columna5)
        lista_tuplas.append(tupla) # Agregar la tupla a la lista
    return lista_tuplas

#Resultado = pregunta_10()
#print(Resultado)

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = leer_data_csv()
    suma_por_letra = {}

    for row in data:
        letra_columna4 = row[3].split(",")  # Obtener la letra de la columna 4
        for i in letra_columna4:
            if i in suma_por_letra.keys():
                suma_por_letra[i] += int(row[1])
            else:
                suma_por_letra[i] = int(row[1])

    # Ordenar el diccionario alfabéticamente por las claves
    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))
    return suma_por_letra_ordenada


#Resultado = pregunta_11()
#print(Resultado)

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = leer_data_csv()
    letras = {}

    for row in data:
        values = row[4].split(",")
        dic_values = dict((rw.split(":")[0],int(rw.split(":")[1])) for rw in values)
        if row[0] in letras.keys():
            letras[row[0]] += sum(dic_values.values())
        else:
            letras[row[0]] = sum(dic_values.values())

    # Ordenar el diccionario alfabéticamente por las claves
    suma_por_clave_ordenada = dict(sorted(letras.items()))
    return suma_por_clave_ordenada

#Resultado = pregunta_12()
#print(Resultado)

if __name__ == "__main__":

    resultado1= pregunta_01()
    print(resultado1)
    
    resultado2 = pregunta_02()
    print(resultado2)

    resultado3 = pregunta_03()
    print(resultado3)

    resultado4 = pregunta_04()
    print(resultado4)

    resultado5 = pregunta_05()
    print(resultado5)

    resultado6= pregunta_06()
    print(resultado6)

    resultado7 = pregunta_07()
    print(resultado7)

    resultado8 = pregunta_08()
    print (resultado8)

    resultado9 = pregunta_09()
    print(resultado9)

    resultado10 = pregunta_10()
    print (resultado10)

    resultado11 = pregunta_11()
    print (resultado11)

    resultado12 = pregunta_12()
    print (resultado12)
