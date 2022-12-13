import pandas as pd 
from alumno import Alumno
from docente import Docente

def filtro():
    df = pd.read_csv("Datos.csv",index_col=0)
    filtro_Edad_Nombres =((df['Edad']>0) & (df['Edad']<120)) &((df['Nombres']!='TRUE') & (df['Nombres']!='FALSE'))
    filtro= (df[filtro_Edad_Nombres])
    filtro.to_csv("DatosActualizados.csv")
    df2 = pd.read_csv("DatosActualizacos.csv")

def main():
    bandera = 1
    while bandera == 1:
        opcion = int(input("Presione los siguientes números para:\n1. Filtrar el archivo csv\n2. Crear lista docentes\n3. Crear lista alumnos\n4. Crear archivos excel\n5. Salir\n>>>: "))
        while opcion < 0 or opcion > 5:
            print("Ingrese una opción válida")
            opcion = int(input("Presione los siguientes números para:\n1. Filtrar el archivo csv\n2. Crear lista docentes\n3. Crear lista alumnos\n4. Crear archivos excel\n5. Salir\n>>>: "))
        if opcion == 1:
            filtro()

        elif opcion == 2:
            lista_docentes = []

        elif opcion == 3:
            lista_alumnos = []
        
        elif opcion == 4:
            pass

        else:
            print("Adiós")
            bandera = 0

main()
