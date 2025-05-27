# Inicialización de variable
comando = ""

# Lista de productos [ID, Nombre, Precio, Cantidad]
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

# Lista de carrito
carrito = []

def lista_productos():
    print("\nBienvenido a la lista de productos de nuestro kiosco. \nEscribí en la consola el número de ID del producto que querés agregar al carrito de compras.\nPodés escribir 'salir' para volver al menú principal.\n")

    # Imprime cada producto de la lista linea por linea
    for producto in productos:
        print(f"{producto}")
        
    id = ""
    while id != "salir":
        # Pregunta el ID del producto a agregar al carrito
        id = input('\nID: ')

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

                    # Agregar al carrito
                    carrito.append((cantidad, producto[1], producto[2]))
                    print(f"Producto {producto[1]} agregado al carrito.")

# Función para ver el carrito
def ver_carrito():

# Función inicial del menú principal
def main(comando):

# Iniciando la función main
main(comando)