

""" Ejercicio
Crear un arreglo de dos dimensiones tamaño 10x4 (o cualquier tamaño) el cual simule un cine con sus filas y columnas.

Crear menú, este debe contener:

1) Registrar rut y nombre del cliente. Nombre mínimo 3 caracteres y el rut debe ser único por cliente y además contener 9 dígitos sin puntos ni guion.
2) Reservar asiento (Solicitar solo el número del asiento), Solo si ya está registrado el rut del cliente puede reservar asiento (Punto 1), y además el asiento debe estar disponible.
3) Consultar estado de los asientos.
4) Eliminar asiento, solicitando el número del asiento.
5) Salir del menú."

"""

import funciones as fn
import numpy as np

filas=10
columnas=4

asientos = np.empty((filas,columnas), dtype=object) # Array bidimensional vacío, usado para generar los asientos.

count=0
for f in range(filas): # Rellenando con números el array bidimensional en orden ascendente.
    for c in range(columnas):
        count+=1
        asientos[f,c] = f"V {count}"  # V = VACÍO / O = OCUPADO
        

listado_nombre=[] # Se irán agregando los nombres registrados
listado_rut=[]    # Se irán agregando los rut registrados

flag= True
while flag == True:
    
    print("\n  ======== Menú ========")
    print("1: Registrar usuario al sistema")
    print("2: Reservar asiento")
    print("3: Consultar estado de los asientos")
    print("4: Eliminar reserva de asiento ")
    print("5: Salir\n  ")
    
    
    try:
        option = int(input("Ingrese una opción: "))
        
        if option == 1:
            
            flag_nombre = False
            while flag_nombre == False:
                nombre= input("\nIngrese su nombre: ")
                flag_nombre, estado = fn.validar_nombre(nombre)
                print(estado)
                
            flag_rut = False
            while flag_rut == False:
                rut= int(input("\nIngrese su rut (sin puntos ni guion) : "))
                flag_rut, estado = fn.validar_rut(rut, listado_rut)
                print(estado)          
            
            estado= fn.registrando_datos(nombre, listado_nombre, rut, listado_rut)
            print(estado)
            
            
        elif option ==2:
            print("\nReservar asiento")
            disponibilidad = fn.disponibilidad(asientos, filas, columnas)
  
            if disponibilidad == True:
                rut= int(input("\nIngrese su rut : "))
                verificar=fn.verificar_registro_rut(rut, listado_rut) 
                
                if verificar == True:
                    print(f"Rut {rut} correcto")
                    numero = int(input("Ingrese el número de asiento que desea registrar : "))
                    fn.registrar_asiento(numero, asientos, filas, columnas, rut, listado_nombre, listado_rut)
 
                if verificar == False:
                    print("\nRut no registrado en el sistema")

            if disponibilidad == False:
                print("\nTodos los asientos están ocupados")
                       
            
        elif option ==3:
            print("\nV = Vacío / O = Ocupado\n")
            print(asientos)
            
            
        elif option ==4:
            print("\nEliminar reserva de asiento")
            num_asiento= int(input("Ingrese el número de asiento : "))
            estado = fn.eliminar_asiento(num_asiento, asientos, filas, columnas)
            print(estado)
            
                     
        elif option ==5:
            print("\nSaliendo del sistema...")
            flag= False
            
            
        else:
            print("\nIngrese un número en el rango de 1 y 5")
            
                   
    except:
        print("\nError: Ingrese un dato válido")