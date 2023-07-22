

def validar_nombre(nombre):   
    if len(nombre) >= 3:
        estado = f"{nombre} ingresado correctamente"
        return True, estado
    
    estado = f"El nombre debe tener un largo mayor a 3 letras"
    return False, estado

        
        
def validar_rut(rut, listado_rut):
    
    for i in listado_rut:   #Si el rut ingresado ya se encuentra en el listado_rut, return false, no es posible agregar ese rut nuevamente     
        if rut == i :
            estado = f"El rut {rut} ya ha sido ingresado anteriormente al sistema"
            return False, estado
               
    rut_str = str(rut)  #Transformando el rut a str, para poder verificar su largo con len
    if len(rut_str) == 9:   
        estado=""
        return True, estado
    
    estado = f"El rut debe tener 9 dígitos"
    return False, estado
        


def registrando_datos(nombre, listado_nombre, rut, listado_rut): #Si se cumplieron las condiciones de las funciones validar_nombre y rut, esta funcion se ejecutara, registrando el nombre y rut en su listado correspondiente
    
    listado_nombre.append(nombre)
    listado_rut.append(rut)
    estado= f"Nombre: {nombre} y Rut: {rut} registrados correctamente"
    return estado



def disponibilidad(asientos, filas, columnas): #Verificar si hay disponibilidad en los asientos antes de realizar una reserva de asiento
    
    for f in range(filas):
        for c in range(columnas):
            if asientos[f,c][0] != "O":  #si el indice 0 de los elementos recorridos en los asientos es diferente de "O" entonces hay disponibilidad aun
                return True
            
    return False  #si se recorrieron todos los elementos en su indice [0] y todos son == "O" entonces esta todo ocupado, return false y no se continua con la reserva
            
        
def verificar_registro_rut(rut, listado_rut): #Verificar si el rut ingresado ya esta registrado o no
    
    for i in listado_rut:
        if i == rut:           
            return True
    
    return False


def registrar_asiento(numero, asientos, filas, columnas, rut, listado_nombre, listado_rut): #Registrar asiento segun numero ingresado por el usuario
    
    #"Formula" ocupada para transformar a partir de un solo numero ingresado, calcular el asiento en un array bidimensional
    fila = (numero -1) // columnas 
    columna = (numero-1) % columnas
    
    if numero < 1:  #necesario porque si el usuario ingresa numeros negativos la funcion asignaba un asiento.
        return print("Número de asiento inválido")
    
    if fila < filas and columna < columnas:  #calcular numero ingresado dentro del rango de asientos
        
        if asientos[fila, columna][0] == "O": #si el numero ingresado ya esta ocupado...
            return print(f"Asiento {numero} ocupado")
        
        elif asientos[fila, columna][0] == "V":           #Si esta vacio, se procede a registrar el asiento con el nombre / recordar que el nombre esta en el mismo indice que el rut, ya que fueron ingresados en el mismo tiempo
            
            posicion = listado_rut.index(rut)  #devuelve el indice del rut en su lista, indice que servira para acceder al nombre en su lista, que fue ingresado al mismo tiempo que el rut(por lo que pertenecen a la misma persona)
            asientos[fila, columna] = f"O {numero} = {listado_nombre[posicion]}" #usando el indice del rut, para acceder al nombre correcto
            return print(f"Asiento {numero} reservado con el nombre {listado_nombre[posicion]}")
        
        else:
            print("Número incorrecto")
        
    else:
        return print("No existe ese n° de asiento")
    


def eliminar_asiento(num_asiento, asientos, filas, columnas):
    
    fila = (num_asiento -1) // columnas 
    columna = (num_asiento-1) % columnas
    
    if num_asiento < 1:
        estado =f"Número de asiento inválido"      
        return estado

    if fila < filas and columna < columnas:
        if asientos[fila,columna][0] == "O": 
            estado =f"El asiento {num_asiento} ha sido eliminado satisfactoriamente" 
            asientos[fila,columna] = f"V {num_asiento}"
            return estado
        else:
            estado =f"El asiento {num_asiento} ya estaba vacío" 
            return estado 
    
    else:
        estado =f"El número {num_asiento} está fuera del rango" 
        return estado