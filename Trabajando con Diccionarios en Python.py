#////////////////////UEA///////////
#Ingenieria en Tecnologias de la Informacion
#Trabajo con diccionario de datos

# Diccionario con la información inicial
datos_personales = {
 'nombre_completo': 'Juan Perez',
 'años': 30,
 'lugar_residencia': 'Madrid',
 'ocupacion': 'Ingeniero de software',
 'contacto': '0989790382'  # Clave existente que se actualizará más adelante
}

# Función para imprimir datos
def imprimir_datos(diccionario):
    print("\nInformación actual:")
    for clave, valor in diccionario.items():
        print(f"{clave.replace('_', ' ').title()}: {valor}")

# Mostrar la información actual
imprimir_datos(datos_personales)

# Función para actualizar datos
def actualizar_dato(clave, mensaje):
    nueva_entrada = input(mensaje)
    datos_personales[clave] = nueva_entrada

# Actualizar la ciudad y la profesión
actualizar_dato('lugar_residencia', "Ingresa una nueva ciudad para reemplazar 'Madrid': ")
actualizar_dato('ocupacion', "Ingresa tu profesión actual para reemplazar 'Ingeniero de software': ")

# Preguntar si quiere actualizar el teléfono
respuesta = input("Tu número de contacto actual es " + datos_personales["contacto"] + ". ¿Quieres actualizarlo? (sí/no): ").lower()
if respuesta == "si":
    actualizar_dato('contacto', "Ingresa tu nuevo número de contacto: ")

# Eliminar la edad si existe en el diccionario
datos_personales.pop('años', None)

# Imprimir la información actualizada
imprimir_datos(datos_personales)
