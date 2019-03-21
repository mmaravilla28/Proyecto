#se declaran las listas a utilizar
Lista_Productos = []
Vector_Productos = []

#buscamos la posición del producto por el nombre
def buscar(codigo):
    posicion = len(Lista_Productos)
    if posicion == 0:
        nombre = ''
    else:
        for Vector_Productos in Lista_Productos:
            if Vector_Productos[0] == codigo:
                nombre = Vector_Productos[1]
            else:
                nombre = ''
    return nombre

#obtenemos los datos del producto a buscar
def buscar_producto(codigo):
    articulo = []
    for p in Lista_Productos:
        if p[0] == codigo:
            articulo.append(p[0])
            articulo.append(p[1])
            articulo.append(p[2])
            articulo.append(p[3])
            articulo.append(p[4])
    return articulo

#se imprimen los datos del producto
def buscar_producto2(codigo):
    existe = False

    for p in Lista_Productos:
        if p[0] == codigo:
            print("Codigo: ", p[0])
            print("Nombre: ", p[1])
            print("Cantidad disponible: ", p[2])
            print("Precio: ", p[3])
            print("Total: ", p[4])
            existe = True
            break

    if existe == False:
        print('EL PRODUCTO INDICADO NO EXISTE')

#se actualiza el inventario de cada producto disponible
def actualizar_inventario(codigo, tipomov, cantidad, total):
    articulo = []
    for p in Lista_Productos:
        if p[0] == codigo:
            Lista_Productos.remove(p)
            cantidad_total = float(p[2])
            total_final = float(p[4])
            if tipomov == 'I':
                cantidad_total += float(cantidad)
                total_final += float(total)
                print(cantidad_total)
                print(total_final)
            else:
                cantidad_total -= float(cantidad)
                total_final -= float(total)
                print(cantidad_total)
                print(total_final)
            if cantidad_total == 0:
                precio = 0
            else:
                precio = total_final / cantidad_total

            articulo.append(p[0])
            articulo.append(p[1])
            articulo.append(cantidad_total)
            articulo.append(precio)
            articulo.append(total_final)
            Lista_Productos.append(articulo)

#se agregan los productos al inventario
def agregar_producto():
    print('\nAGREGAR PRODUCTOS\n')
    codigo = input("Digite el código del producto: ")
    nombre = buscar(codigo)

    if nombre == '':
        nombre = input("Digite la descripción del producto: ")
    else:
        print("Nombre del Producto: ", nombre)

    cantidad = input("Digite la cantidad del producto: ")
    precio = input("Digite el Precio del producto: ")
    total = float(cantidad) * float(precio)

    Vector_Productos.append(codigo)
    Vector_Productos.append(nombre)
    Vector_Productos.append(cantidad)
    Vector_Productos.append(precio)
    Vector_Productos.append(total)
    Lista_Productos.append(Vector_Productos)

#se elimina el producto del inventario
def eliminar_producto():
    lista = []

    print('\nELIMINAR PRODUCTO\n')
    codigo = input("Digite el código del producto: ")
    producto = buscar_producto(codigo)

    if len(producto) > 0:
        print("Nombre del Producto: ", producto[1])
        print("Precio del Producto: ", producto[3])

        cantidad = float(input("Digite la cantidad a eliminar: "))
        total = float(producto[3]) * cantidad

        lista.append("E")
        lista.append(codigo)
        lista.append(producto[1])
        lista.append(cantidad)
        lista.append(float(producto[3]))
        lista.append(total)
        actualizar_inventario(codigo, 'E', cantidad, total)
        Lista_Productos.append(lista)
    else:
        print("\nEL PRODUCTO INDICADO NO EXISTE EN EL INVENTARIO")

#Menú Principal de Opciones
while True:
    print('\nSISTEMA DE INVENTARIO\n')
    print('MENÚ PRINCIPAL\n')
    print('1. AGREGAR PRODUCTOS')
    print('2. ELIMINAR PRODUCTOS')
    print('3. BÚSCAR PRODUCTOS')
    print('4. SALIR\n')
    opcion = input('SELECCIONE UNA OPCIÓN VÁLIDA POR FAVOR: ')

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        eliminar_producto()
    elif opcion == '3':
        codigo = input("\nDIGITE EL CÓDIGO DEL PRODUCTO A BUSCAR: ")
        buscar_producto2(codigo)
    elif opcion == '4':
        break
    else:
        print('\nOPCIÓN NO VÁLIDA, INTENTE DE NUEVO')