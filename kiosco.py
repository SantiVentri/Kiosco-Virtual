# Inicialización de variable
comando = ""

# Lista de productos
productos = [
    ["1", "Galletitas Oreo", 550],
    ["2", "Chupetín Pico Dulce", 100],
    ["3", "Alfajor Jorgito", 300],
    ["4", "Coca-Cola 500ml", 750],
    ["5", "Papas Lays", 800],
    ["6", "Chicle Topline", 150],
    ["7", "Bon o Bon", 200],
    ["8", "Agua mineral 500ml", 500],
    ["9", "Tita", 180],
    ["10", "Palito helado", 600],
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
            # Busca por cada producto si el ID coincide con el que ingresó el usuario
            for producto in productos:
                # Si coincide, lo agrega al carrito
                if id == producto[0]:
                    cantidad = int(input('Ingresar cantidad de este producto: '))
                    carrito.append((cantidad, producto[1]))

# Función para ver el carrito
def ver_carrito():

# Función inicial del menú principal
def main(comando):

# Iniciando la función main
main(comando)