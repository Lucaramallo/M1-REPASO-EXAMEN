# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV.
# EJ: 'datasets/xxxxxxxxxx.csv'

from xml.dom.minidom import Entity
import pandas as pd
import numpy as np

def Ret_Pregunta01( ):
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sean Colombia o México retornando ese valor en un dato de tipo tupla (catidad de registros Colombia, catidad de registros México).
    Pista: averiguar la funcion Shape
    '''
    # #Tu código aca:
    
    # Debes utilizar Pandas
    # para ingestar en un objeto Dataframe el contenido del archivo provisto Fuentes_Consumo_Energia.csv".
   
    
    import pandas as pd

    df1 = pd.read_csv(r'./datasets/Fuentes_Consumo_Energia.csv', sep = ',',encoding='UTF-8')
    
   
    df1_limpio = df1.dropna().drop_duplicates()
    
   

    #print(df1.info())

    # Esta función debe informar la cantidad de registros cuya entidad sean Colombia o México
    # retornando ese valor en un dato de tipo tupla

    resultado_colombia = df1_limpio[(df1_limpio['Entity'] == 'Colombia') ].shape[0]
    
    resultado_mexico = df1_limpio[(df1_limpio['Entity'] == 'Mexico') ].shape[0]
    
    resultado1 = (resultado_colombia, resultado_mexico)
    #print(type(resultado))
    #print(resultado)
    # (catidad de registros Colombia, catidad de registros México).
    # 
    # Pista: averiguar la funcion Shape


    print(resultado1)
    return resultado1

#Ret_Pregunta01() 



def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    # #Tu código aca:
    # Debes utilizar Pandas
    
    #  para ingestar en un objeto Dataframe el contenido del archivo provisto "Fuentes_Consumo_Energia.csv".
    
    import pandas as pd

    df2 = pd.read_csv(r'./datasets/Fuentes_Consumo_Energia.csv', sep = ',',encoding='UTF-8')
    df2_limpio = df2.dropna().drop_duplicates()
    
    # Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    # retornando ese valor en un dato de tipo entero.

    code_column = df2_limpio.pop(item= 'Code')
    
    entity_colum = df2_limpio.pop(item= 'Entity')

    #resultado2 = type(df2_limpio.shape[1]) verificacion tipy int
    resultado2 = df2_limpio.shape[1]
    
    
    # Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    # retornando ese valor en un dato de tipo entero.

    print(resultado2)
    return resultado2

#Ret_Pregunta02() 



def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros de la columna Year sin tener en cuenta aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero.
    '''
    # #Tu código aca:
    # Debes utilizar Pandas
    
    #  para ingestar en un objeto Dataframe el contenido del archivo provisto "Fuentes_Consumo_Energia.csv".
    
    import pandas as pd

    df3 = pd.read_csv(r'./datasets/Fuentes_Consumo_Energia.csv', sep = ',',encoding='UTF-8')
    df3_limpio = df3.dropna().drop_duplicates()
    resultado3 = df3['Year'].shape[0]

    # Esta función debe informar la cantidad de registros de la columna Year
    
    # sin tener en cuenta aquellos con valores faltantes
    # retornando ese valor en un dato de tipo entero.
    print (resultado3)
    return resultado3

#Ret_Pregunta03() ok.

def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    # #Tu código aca:
    # Debes utilizar Pandas
    
    #  para ingestar en un objeto Dataframe el contenido del archivo provisto "Fuentes_Consumo_Energia.csv".
    
    import pandas as pd

    df4 = pd.read_csv(r'./datasets/Fuentes_Consumo_Energia.csv', sep = ',',encoding='UTF-8')
    df4_limpio = df4.dropna().drop_duplicates()
    
    

    # El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    # buscar proporciones entre ellos.  
    # 
    #  la fórmula de conversión es:
    # 277.778 Teravatios/Hora (TWh) = 1 Exajulio
    

    # Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    # son los que debo transformar a teravatios /hora la conversion:
    
    # los terminados en "_TWh" corresponden a Teravatios/Hora 
    
    df4_limpio['Coal_Consumption_EJ'] = df4_limpio['Coal_Consumption_EJ']*277778
    
    df4_limpio['Gas_Consumption_EJ'] = df4_limpio['Gas_Consumption_EJ']*277778

    df4_limpio['Oil_Consumption_EJ'] = df4_limpio['Oil_Consumption_EJ']*277778
    
   
   
   
    # La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    # y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    # (convirtiendo a esta medida los que están en Exajulios)
    



    df4_limpio['Consumo_Total'] = df4_limpio['Coal_Consumption_EJ'] + df4_limpio['Gas_Consumption_EJ'] +  df4_limpio['Oil_Consumption_EJ']        #suma de las dos columnas guardadas en nueva ccol.
   
    





    # Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    # redondeado a 2 decimales, retornando ese valor en un dato de tipo float.

    nuevo_df4 = (df4_limpio[(df4_limpio['Entity'] == 'World') & (df4_limpio['Year'] == 2019)])
    resultado4 = nuevo_df4['Consumo_Total'].round(decimals= 2).astype(float)
    resultado4 = resultado4.round(decimals=3).astype(float)
   
    #print(resultado4)
    return resultado4

#Ret_Pregunta04()

def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía hídrica (Hydro_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    
    # Debes utilizar Pandas
    
    #  para ingestar en un objeto Dataframe el contenido del archivo provisto "Fuentes_Consumo_Energia.csv".
    
    import pandas as pd

    df5 = pd.read_csv(r'./datasets/Fuentes_Consumo_Energia.csv', sep = ',',encoding='UTF-8')
    df5_limpio = df5.dropna().drop_duplicates()
    
    #resultado5 = df5_limpio


    # Esta función debe informar el año de mayor generación de energía hídrica (Hydro_Generation_TWh)
    
    resultado5 = df5_limpio[['Entity'] == ['Europe']] =  df5_limpio['Hydro_Generation_TWh'].max()
    
    resultado5_1 = resultado5.astype(int)
    # para la entidad 'Europe' retornando ese valor en un dato de tipo entero.

    


    #print(resultado5_1)
    return resultado5_1

#Ret_Pregunta05()

def Ret_Pregunta06(m1, m2, m3):
    '''
    Esta función recibe tres array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        n3 = np.array([1,1],[2,2])
        print(Ret_Pregunta06(n1,n2,n3))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1,n3))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:

    # Esta función recibe tres array de Numpy de 2
    # dimensiones cada uno,
    import numpy as np

    if m1.shape[1] == m2.shape[0] and m2.shape[1] == m3.shape[0]:
        resultado6 = True
    else:
        resultado6 = False
        
    #print(m1.shape)
    #print(m2.shape)
    #print(m3.shape)

    
    #  y devuelve el valor booleano
    # True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    # y el valor booleano False si no lo es
    # Ej:
    #     n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
    #     n2 = np.array([[3,3],[4,4],[5,5]])
    #     n3 = np.array([1,1],[2,2])
    #     print(Ret_Pregunta06(n1,n2,n3))
    #         True            -> Valor devuelto por la función en este ejemplo
    #     print(Ret_Pregunta06(n2,n1,n3))
    #         False            -> Valor devuelto por la función en este ejemplo
    
    

    #print(resultado6)
    return resultado6



def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galcia SA. Esta función debe tomar la columna máximo y 
    devolver la suma de los valores de esta, con 4 decimales después del punto, redondeado.
    '''
    # #Tu código aca:
    # Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    # "GGAL - Cotizaciones historicas.csv". 
    import pandas as pd
    # Este csv contiene información de cotización de la 
    # acción del Banco Galcia SA.
    df7 = pd.read_csv(r'./datasets/GGAL - Cotizaciones historicas.csv', sep = ',',encoding='UTF-8')
    df7_limpio = df7.dropna().drop_duplicates()
    #resultado7 =df7_limpio.
     
    
    # Esta función debe tomar la columna máximo y 
    # devolver la suma de los valores de esta, con 4 decimales después del punto, redondeado.
    
    resultado7 = df7_limpio['maximo'].sum().round(decimals= 4)
   
    #print(resultado7)
    return resultado7

#Ret_Pregunta07()

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero.
    '''
    # #Tu código aca:
    # Debes utilizar Pandas
    
    #  para ingestar en un objeto Dataframe el contenido del archivo provisto "Fuentes_Consumo_Energia.csv".
    
    import pandas as pd

    df8 = pd.read_csv(r'./datasets/Fuentes_Consumo_Energia.csv', sep = ',',encoding='UTF-8')
    shapedf8 =df8.dropna()
    shapedf8 = shapedf8.drop_duplicates()
    shapedf8.shape
    
    can_ent = shapedf8[1]
    can_ent_type = type(can_ent)
    # Esta función debe informar la cantidad de entidades diferentes
    # que están presentes en el dataset
     
    
    
    # retornando ese valor en un dato de tipo entero.


    
    
    return can_ent

#Ret_Pregunta08() #ok

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe retornar: score_promedio_femenino y score_promedio_masculino en formato tupla, teniendo en cuenta que no debe haber valores repetidos.'''
    #Tu código aca:
    
    # Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    # "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".

    import pandas as pd

    df_T1 = pd.read_csv(r'./datasets/Tabla1_ejercicio.csv', sep = ';',encoding='UTF-8')
    df_T1_lim = df_T1.dropna().drop_duplicates()

    #rta.info()

    df_T2 = pd.read_csv(r'./datasets/Tabla2_ejercicio.csv', sep = ';',encoding='UTF-8')
    df_T2_lim = df_T2.dropna().drop_duplicates()

    #df_T1_lim.info()
    
    #df_T2_lim.info()
    
    #debo concatenar bien los dos df...

    df_9 = pd.merge(df_T1_lim, df_T2_lim, on=['pers_id'])
    df_9.drop_duplicates()
    df_9.dropna()
    

    
    # Esta función debe retornar: score_promedio_femenino y score_promedio_masculino en formato tupla,
    #  teniendo en cuenta que no debe haber valores repetidos.'''
    df_9_1 = pd.DataFrame(df_9.groupby('sexo')['score'].mean())   

    tupla_rta = tuple(df_9_1['score'].to_dict().items())
    tupla_rta = tupla_rta[0][1],tupla_rta[1][1]

    return tupla_rta
    
#Ret_Pregunta09()



def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:

    class Nodo():
        def __init__(self, dato):
            self.__dato = dato
            self.__siguiente = None

        def getDato(self):
            return self.__dato

        def getSiguiente(self):
            return self.__siguiente

        def setDato(self, val):
            self.__dato = val

        def setSiguiente(self, val):
            self.__siguiente = val

    class Lista():
        def __init__(self):
            self.__cabecera = None

        def agregarElemento(self,dato):
            if (self.__cabecera != None):
                puntero = self.__cabecera
                while(puntero != None):
                    if(puntero.getSiguiente() == None):
                        puntero.setSiguiente(Nodo(dato))
                        break
                    puntero = puntero.getSiguiente()
            else:
                self.__cabecera = Nodo(dato)

        def contarElementos(self):
            if (self.__cabecera == None):
                return 0
            else:
                contador = 1
                puntero = self.__cabecera
                while(puntero.getSiguiente() != None):
                    contador += 1
                    puntero = puntero.getSiguiente()
                return contador

        def getCabecera(self):
            return self.__cabecera
    
lis = Lista()
    lista.agregarElemento(1)
    lista.agregarElemento(2)
    lista.agregarElemento(3)
    print(Ret_Pregunta10(lista))

    #return 'Funcion incompleta

