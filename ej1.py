mi_biblioteca=0

print(" - - - - - - - - - - - - - -")
print("|       ETec Station      |")
print(" - - - - - - - - - - - - - -")

menu={
    "1" : "Tienda",
    "2" : "Juegos",
    "3" : "Salir"
}
print(menu)

tienda={
    "accion" : ["1. Mono enojado", " 2. Gato ninja", " 3. Samurai", " 4. Free fire"],
    "terror" : [" 1. La monja", " 2. Los payasos", " 3. El conjuro", " 4. Five nights at Freddy"],
    "ciencia ficcion" : [" 1. Rol del ayudante de Ironman", " 2. Los inicios de Star Wars", " 3. Las aventuras de Spiderman", " 4. Los vengadores"]
}

biblioteca={
    mi_biblioteca : []
}

respuesta=input("Ingrese una opción: ")
if respuesta == "1":
    print(tienda)
    rta_tienda=input("Ingrese el género que quiera agregar a su compra: ")
    if rta_tienda in tienda:
        print("Los productos disponibles en el género", rta_tienda, "son:", tienda[rta_tienda])
        producto=input("Ingrese el nombre del producto que quiera comprar: ")
        if producto in tienda[rta_tienda]:
            biblioteca[mi_biblioteca].append(producto)
            print("Se ha agregado a su biblioteca")
        else:
            print("El producto ingresado no está disponible en el género seleccionado.")
    else:
        print("El género ingresado no está disponible en la tienda.")
elif respuesta == "2":
    print(mi_biblioteca)

