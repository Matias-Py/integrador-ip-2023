carrito = ["zapatos"]
camisas = ["camisetas", "camisas de vestir", "camisas informales", "camisas de manga corta","manga larga"]
pantalones = ["pantalones vaqueros", "pantalones chinos", "pantalones de vestir","pantalones cortos"]
vestidos = ["vestidos casuales", "vestidos de cóctel", "vestidos de noche", "vestidos formales", "vestidos estampados"]
trajes = ["trajes de dos piezas", "trajes de tres piezas", "trajes formales", "trajes de oficina"]
abrigos = ["abrigos","chaquetas","chaquetones", "gabardinas", "chalecos"]
deportiva = ["camisetas deportivas", "pantalones deportivos", "sudaderas", "leggings deportivos", "ropa de yoga"]
dormir = ["pijamas","camisones, batas","pantalones de pijama", "conjuntos de dormir"]
accesorios = ["sombreros", "gorras", "bufandas", "guantes", "cinturones", "joyas, bolsos"]


def agregarCarrito(nombre,precio):
    carrito.append([nombre,precio])

def quitarDelCarrito(nombre):
    for producto in carrito:
        if producto[0] == nombre:
            carrito.remove(producto)
    

print("-------------TIENDA ABIBAS-------------")
while True:
    menu = input("""
                1- Ver catalogo
                2- Ver carrito
                3- Finalizar compra
                Tu eleccion: """)
    if menu == "1":
        opcion = input("""
                1- Camisas
                2- Pantalones
                3- Vestidos
                4- Trajes
                5- Abrigos
                6- Ropa deportiva
                7- Ropa de dormir
                8- Accesorios
                Tu eleccion: """)

        match opcion:
            case "1":
                print("-------------Camisas-------------")
                for item in camisas:
                    print("*",item)
            case "2":
                print("-------------Pantalones-------------")
                for item in pantalones:
                    print("*",item)
            case "3":
                print("-------------Vestidos-------------")
                for item in vestidos:
                    print("*",item)
            case "4":
                print("-------------Trajes-------------")
                for item in trajes:
                    print("*",item)
            case "5":
                print("-------------Abrigos-------------")
                for item in abrigos:
                    print("*",item)
            case "6":
                print("-------------Ropa deportiva-------------")
                for item in deportiva:
                    print("*",item)
            case "7":
                print("-------------Ropa de dormir-------------")
                for item in dormir:
                    print(item)
            case "8":
                print("-------------Accesorios-------------")
                for item in accesorios:
                    print(item)
    if menu == "2":
        print("-------------CARRITO-------------")
        for producto in carrito:
            print(producto)
            
    if menu == "3":
        print("-------------PROGRAMA FINALIZADO-------------")
        break