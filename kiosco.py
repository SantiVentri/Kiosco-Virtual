import random

# Lista de productos [ID, Nombre, Precio, Stock]
productos = [
    ["1", "Galletitas Oreo", 550, 55],
    ["2", "Chupetín Pico Dulce", 100, 80],
    ["3", "Alfajor Jorgito", 300, 120],
    ["4", "Coca-Cola 500ml", 750, 100],
    ["5", "Papas Lays", 800, 150],
    ["6", "Chicle Topline", 150, 40],
    ["7", "Bon o Bon", 200, 90],
    ["8", "Agua mineral 500ml", 500, 70],
    ["9", "Tita", 180, 60],
    ["10", "Palito helado", 600, 200],
]

# Lista de carrito [Cantidad, Nombre, Precio]
carrito = []

def lista_productos():
    print("\n------------------- Lista de productos -------------------\n")
    print("Bienvenido a la lista de productos de nuestro kiosco.\n\nEscribí en la consola el número de ID del producto que querés agregar al carrito de compras.\n\nPodés escribir 'salir' para volver al menú principal.\n")

    # Imprime cada producto de la lista linea por linea
    print("['ID', Nombre, Precio, Cantidad restante]\n")
    for producto in productos:
        print(f"{producto}")
    print("\n")
        
    id = ""
    while id != "salir":
        # Pregunta el ID del producto a agregar al carrito
        id = input('ID: ')

        if id == "salir":
            print("\nSaliendo de la lista de productos...\n")
        else:
            # Busca en la lista de productos producto por producto hasta que el ID ingresado coincida con el ID de algún producto
            for producto in productos:
                if id == producto[0]:
                    cantidad = int(input(f'Ingresar cantidad de este producto (Unidades restantes: {producto[3]}): '))

                    # Si el usuario pide más de la cantidad disponible o 0
                    while cantidad > producto[3] or cantidad == 0:
                        print(f"Ingresar una cantidad válida.")
                        cantidad = int(input(f'Ingresar cantidad de este producto (Unidades restantes: {producto[3]}): '))

                    # Se añade el producto al carrito
                    agregar_producto_carrito(cantidad, producto[1], producto[2])

                    # Se resta del stock la cantidad reservada a comprar
                    producto[3] -= cantidad
            
            print("Escribí en la consola el número de ID del producto que querés agregar al carrito de compras.\nPodés escribir 'salir' para volver al menú principal.\n")

# Agregar al carrito
def agregar_producto_carrito(cantidad, nombre, precio):
    carrito.append((cantidad, nombre, precio))
    print(f"\n* Producto {nombre} agregado al carrito.")
    organizar_carrito()

# Función para ver el carrito
def ver_carrito():
    print("\n------------------- Carrito de compras -------------------\n")
    if len(carrito) == 0:
        print("\nEl carrito está vacío.\n")
    else:
        total_carrito = 0
        # Imprimir carrito
        for item in carrito:
            total = item[0] * item[2]
            print(f"{item[0]} x {item[1]} - Total: ARS${total}")

        # Calcular el total del carrito
        for item in carrito:
            total_carrito += item[0] * item[2]
        print(f"\nTotal del carrito: ARS${total_carrito}\n")

        opcion = ""
        while opcion != "salir":
            print("¿Querés sacar algún producto del carrito?\n(Escribi el número del producto que quieras eliminar o 'salir' para volver al menú)\n")
            opcion = input(">> ")
            if opcion == "salir":
                print('Saliendo del carrito...')
            else:
                opcion = int(opcion)
                for i in range(len(carrito)):
                    producto = carrito[opcion]
                    if opcion == i:
                        carrito.pop(opcion)
                        print(f"* {producto[1]} eliminado del carrito.\n")

def organizar_carrito():
    print("\nOrganizando el carrito de mayor a menor según la cantidad...")

    # Método de inserción
    for i in range(1, len(carrito)):
        aux = carrito[i]
        j = i - 1
        while j >= 0 and carrito[j][0] < aux[0]:
            carrito[j + 1] = carrito[j]
            j -= 1
        carrito[j + 1] = aux
    print("* Carrito organizado.\n")


def generar_combo_dia():
    numeros = []
    while len(numeros) < 3:
        n = random.randint(0, len(productos)-1) 
        if n not in numeros:
            numeros.append(n)

    combo_dia = [productos[i] for i in numeros]
    return combo_dia

def ver_combo(combo_dia):
    print("\n------------------- Combo del Día -------------------\n")
    total = 0
    for item in combo_dia:
        print(f"- {item[1]} (Precio: ARS${item[2]})")
        total += item[2]

    descuento_porcentaje = 10  # descuento fijo 10%
    descuento = int(total * descuento_porcentaje / 100)
    total_con_descuento = total - descuento

    print(f"\nPrecio normal: ARS${total}")
    print(f"Descuento aplicado: {descuento_porcentaje}% (-ARS${descuento})")
    print(f"Total con descuento: ARS${total_con_descuento}")

    decision = input("\n¿Querés agregar el combo al carrito? (sí/no): ").lower()
    if decision == "si" or decision == "sí":
        # Agregamos cada producto con cantidad 1 y el precio original (sin descuento individual)
        for item in combo_dia:
            # Antes de agregar verificamos stock
            precio = item[2] * 0.9
            if item[3] > 0:
                agregar_producto_carrito(1, item[1], precio)
                item[3] -= 1
            else:
                print(f"No hay stock suficiente para {item[1]}, no se agregó al combo.")
        print("Combo del día agregado al carrito.\n")
    else:
        print("Combo no agregado.\n")

# Función inicial del menú principal
def main():
    combo_dia = generar_combo_dia()
    print('Bienvenido al kiosco virtual.')
    
    opcion = ""

    while opcion != "salir":
        print("\n------------------- Menú Principal -------------------\n")
        print("1. Ver productos y agregar al carrito")
        print("2. Ver carrito de compras")
        print("3. Ver el combo del día")
        print("\nPodes escribir 'salir' para terminar el programa")

        opcion = input("\nSeleccioná una opción: ")

        if opcion == "salir":
            print("¡Gracias por usar el kiosco virtual!")
        elif opcion == "1":
            lista_productos()
        elif opcion == "2":
            ver_carrito()
        elif opcion == "3":
            ver_combo(combo_dia)
        else:
            print("Opción no válida. Intentá de nuevo.")

# Iniciando la función main
main()
