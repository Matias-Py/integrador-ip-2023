carrito = []
camisas = ["camisetas", "camisas de vestir", "camisas informales", "camisas de manga corta","manga larga"]
pantalones = ["pantalones vaqueros", "pantalones chinos", "pantalones de vestir","pantalones cortos"]
vestidos = ["vestidos casuales", "vestidos de cóctel", "vestidos de noche", "vestidos formales", "vestidos estampados"]
trajes = ["trajes de dos piezas", "trajes de tres piezas", "trajes formales", "trajes de oficina"]
abrigos = ["abrigos","chaquetas","chaquetones", "gabardinas", "chalecos"]
deportiva = ["camisetas deportivas", "pantalones deportivos", "sudaderas", "leggings deportivos", "ropa de yoga"]
dormir = ["pijamas","camisones, batas","pantalones de pijama", "conjuntos de dormir"]
accesorios = ["sombreros", "gorras", "bufandas", "guantes", "cinturones", "joyas, bolsos"]


def agregarCarrito(producto):
    carrito.append([producto])

def quitarDelCarrito(nombre):
    for producto in carrito:
        if producto[0] == nombre:
            carrito.remove(producto)
    

print("-------------TIENDA ABIBAS-------------")
while True:
    menu = input("""
                -------------Inicio-------------
                1- Ver catalogo
                2- Ver carrito
                3- Finalizar compra
                Tu eleccion: """)
    if menu == "1":
        opcion = input("""
                -------------Categorias-------------
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
                    print("*",item.ljust(20))
                    
                agregar = input("""
                    ¿Deseas agregar algun producto al carrito?
                    1- Si
                    2- No
                    Su eleccion: """)
                
                if agregar == "1":
                    contador = 1
                    for item in camisas:
                        print(contador,"-",item.ljust(20))
                        contador = contador + 1
                    seleccion = input("""
                    ¿Que producto agregar al carrito?
                    su eleccion: """)
                    agregarCarrito(camisas[int(seleccion)-1])
                    
                    
            case "2":
                print("-------------Pantalones-------------")
                for item in pantalones:
                    print("*",item.ljust(20))
                
                agregar = input("""
                    ¿Deseas agregar algun producto al carrito?
                    1- Si
                    2- No
                    Su eleccion: """)

                if agregar == "1":
                    contador = 1
                    for item in pantalones:
                        print(contador,"-",item.ljust(20))
                        contador = contador + 1
                    seleccion = input("""
                    ¿Que producto agregar al carrito?
                    su eleccion: """)
                    agregarCarrito(pantalones[int(seleccion)-1])
                    
            case "3":
                print("-------------Vestidos-------------")
                for item in vestidos:
                    print("*",item.ljust(20))
                
                agregar = input("""
                    ¿Deseas agregar algun producto al carrito?
                    1- Si
                    2- No
                    Su eleccion: """)

                if agregar == "1":
                    contador = 1
                    for item in vestidos:
                        print(contador,"-",item.ljust(20))
                        contador = contador + 1
                    seleccion = input("""
                    ¿Que producto agregar al carrito?
                    su eleccion: """)
                    agregarCarrito(vestidos[int(seleccion)-1])
                    
            case "4":
                print("-------------Trajes-------------")
                for item in trajes:
                    print("*",item.ljust(20))
                    
                agregar = input("""
                    ¿Deseas agregar algun producto al carrito?
                    1- Si
                    2- No
                    Su eleccion: """)

                if agregar == "1":
                    contador = 1
                    for item in trajes:
                        print(contador,"-",item.ljust(20))
                        contador = contador + 1
                    seleccion = input("""
                    ¿Que producto agregar al carrito?
                    su eleccion: """)
                    agregarCarrito(trajes[int(seleccion)-1])
                    
            case "5":
                print("-------------Abrigos-------------")
                for item in abrigos:
                    print("*",item.ljust(20))
                    
                agregar = input("""
                    ¿Deseas agregar algun producto al carrito?
                    1- Si
                    2- No
                    Su eleccion: """)

                if agregar == "1":
                    contador = 1
                    for item in abrigos:
                        print(contador,"-",item.ljust(20))
                        contador = contador + 1
                    seleccion = input("""
                    ¿Que producto agregar al carrito?
                    su eleccion: """)
                    agregarCarrito(abrigos[int(seleccion)-1])
                    
            case "6":
                print("-------------Ropa deportiva-------------")
                for item in deportiva:
                    print("*",item.ljust(20))
                    
                agregar = input("""
                    ¿Deseas agregar algun producto al carrito?
                    1- Si
                    2- No
                    Su eleccion: """)

                if agregar == "1":
                    contador = 1
                    for item in deportiva:
                        print(contador,"-",item.ljust(20))
                        contador = contador + 1
                    seleccion = input("""
                    ¿Que producto agregar al carrito?
                    su eleccion: """)
                    agregarCarrito(deportiva[int(seleccion)-1])
                    
            case "7":
                print("-------------Ropa de dormir-------------")
                for item in dormir:
                    print(item)
                    
                agregar = input("""
                    ¿Deseas agregar algun producto al carrito?
                    1- Si
                    2- No
                    Su eleccion: """)

                if agregar == "1":
                    contador = 1
                    for item in dormir:
                        print(contador,"-",item.ljust(20))
                        contador = contador + 1
                    seleccion = input("""
                    ¿Que producto agregar al carrito?
                    su eleccion: """)
                    agregarCarrito(dormir[int(seleccion)-1])
                
            case "8":
                print("-------------Accesorios-------------")
                for item in accesorios:
                    print(item.ljust(20))
                
                agregar = input("""
                    ¿Deseas agregar algun producto al carrito?
                    1- Si
                    2- No
                    Su eleccion: """)

                if agregar == "1":
                    contador = 1
                    for item in accesorios:
                        print(contador,"-",item.ljust(20))
                        contador = contador + 1
                    seleccion = input("""
                    ¿Que producto agregar al carrito?
                    su eleccion: """)
                    agregarCarrito(accesorios[int(seleccion)-1])
                
    if menu == "2":
        
        print("                -------------CARRITO-------------")
        for producto in carrito:
            print("               *",producto[0])
        eliminar = input("""
                         ¿Deseas quitar algun producto del carrito?
                         1- Si
                         2- No
                         """)
        if eliminar == "1":
            print("                ¿Que elemento deseas eliminar?")
            contador = 1
            respuesta = ""
            for item in carrito:
                print("                ",contador,"-",item[0])
                contador = contador + 1
            
            
    if menu == "3":
        print("-------------PROGRAMA FINALIZADO-------------")
        break
